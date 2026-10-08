"""Fetch the plates into assets/plates/ (<id>.jpg, max 1600 px, and <id>_t.jpg) and write data/plates.json.

Two kinds of source:
- Wikimedia Commons: the file page must carry a public-domain or CC0 licence template (checked here).
- A federal item page outside Commons (USGS ScienceBase): its rights field must say the item is in the
  U.S. public domain (checked here).
- A page of a scanned book or journal on archive.org: its catalogue date must be before 1931, i.e. an American
  publication in the public domain (checked here); the illustration is cut from the page image.
Run from the repository root:  python tools/make-plates.py      (--meta prints Commons date/author/credit)
"""
import io
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "plates"
UA = {"User-Agent": "SeaGoingRailroad/0.1 (educational; pantaleon fassbender)"}
OK = re.compile(r"\{\{\s*(PD-|Licensed-PD|cc-zero|CC-zero|CC-0|Cc-zero|PD\b|Public domain)", re.I)
BAD = re.compile(r"cc-by|GFDL|Licence Ouverte", re.I)

CREDIT = ("Plates: public-domain images from Wikimedia Commons (the licence checked on each file page) and from the "
          "U.S. Geological Survey's photographic library (a federal work in the public domain), each named in its "
          "caption with the original. Resized for this site.")

# id, source ("commons:<file>", "sciencebase:<item id>" or "archive:<item>:<page image n>"), title, side, caption[, crop as fractions l, t, r, b]
PLATES = [
    ("vaughan1908", "sciencebase:51ddc69be4b0f72b4472100b",
     "The arches on Long Key, 1908", "company",
     "Photograph by the geologist T. Wayland Vaughan of the U.S. Geological Survey, 1908: arches of the Long Key viaduct standing in open water, the year the line reached Knight's Key. The viaduct had about 180 arches of fifty feet."),
    ("flagler1909", "commons:H.M. Flagler's Special, first train crossing Long Key Viaduct, 2.7 miles long, Long Key, Fla. LCCN2005694817.jpg",
     "Flagler's special on the Long Key viaduct", "company",
     "'H.M. Flagler's Special, first train crossing Long Key Viaduct, 2.7 miles long.' Photograph by John N. Chamberlain, 1909 (Library of Congress). The line reached Knight's Key in February 1908; Key West only in 1912."),
    ("arch1914", "commons:NSRW Florida Keys Railroad - building arch.jpg",
     "Building an arch", "labour",
     "From The New Student's Reference Work (1914): falsework and forms for one of the concrete arches. The engineering press counted some five hundred arches over about six miles."),
    ("pier1914", "commons:NSRW Florida Keys Railroad - building pier.jpg",
     "Building a pier", "labour",
     "From The New Student's Reference Work (1914): a reinforced concrete pier in its cofferdam, the work that the storms of 1906 and 1909 swept away and that had to be begun again."),
    ("map1905", "archive:sim_railway-age_1905-10-06_39_14:15",
     "The projected line, 1905", "company",
     "'Map of Florida Keys Showing Projected Extension of the Florida East Coast to Key West', The Railroad Gazette, 6 October 1905, p. 324: the line from Homestead across Key Largo and down the keys, 'completed line' and 'proposed line', six months after work began.",
     (0.10, 0.41, 0.90, 0.605)),
    ("quarterboat1912", "archive:keywestextension00flor:17",
     "A floating camp or quarterboat", "labour",
     "'Floating camp or quarterboat': photograph from the railway's booklet for the opening, 1912. The men building the viaducts lived on such boats, moored behind the keys; in October 1906 a hurricane carried them out to sea.",
     (0.155, 0.352, 0.94, 0.604)),
    ("archcenter1906", "archive:engineering-record_1906-10-20_54_16:3",
     "Arch center and spandrel wall forms, 1906", "labour",
     "'Arch Center and Spandrel Wall Forms Under Construction': the timber falsework for one of the concrete arches, with carpenters at work. From George P. Carver's article in The Engineering Record, 20 October 1906, p. 424.",
     (0.094, 0.061, 0.652, 0.30)),
    ("bahiahonda1912", "archive:sim_railway-age_1912-05-10_52_19:10",
     "The Bahia Honda bridge, 1912", "company",
     "'Bahia Honda Bridge, Only Truss Bridge on Extension': the steel trusses over the deepest water of the line, where some piers stand 30 feet below tide. Railway Age Gazette, 10 May 1912, p. 1039.",
     (0.074, 0.435, 0.871, 0.59)),
    ("foremenboat1906", "archive:sim_railway-age_1906-04-20_40_16:12",
     "A houseboat for foremen, 1906", "labour",
     "'Houseboat for Foremen': a two-storey houseboat moored at the shore, from Harry C. Smith's report in The Railroad Gazette, 20 April 1906, p. 405. Six months later the hurricane of October 1906 tore such boats from their moorings.",
     (0.538, 0.659, 0.896, 0.889)),
    ("bigpine1907", "archive:sim_railway-age_1907-04-26_42_17:16",
     "Big Pine camp, 1907", "labour",
     "'Big Pine Camp': a construction camp under the trees on Big Pine Key, from F. E. Spooner's report in The Railroad Gazette, 26 April 1907, p. 583. Spooner visited 'nearly every one of the 25 or more construction camps'.",
     (0.137, 0.715, 0.49, 0.915)),
    ("arrival1912", "commons:Arrival of first train at Key West, Fla., over sea, Florida East Coast R. R., Jan. 22, (19)12 LCCN2007660721.tif",
     "The first train at Key West, 22 January 1912", "keys",
     "'Arrival of first train at Key West, Fla., over sea, Florida East Coast R. R., Jan. 22, 1912': panoramic photograph, Library of Congress, cut from its mount. The company's booklet of the same year puts the line at 128.4 miles from Homestead.",
     (0.07, 0.345, 0.96, 0.615)),
    ("flaglerparty1912", "commons:Mr. H. M. Flagler and party leaving first train to arrive at Key West, Fla. Oversea Florida East Coast R. R LCCN2007660733.tif",
     "Flagler and his party leave the first train", "company",
     "'Mr. H. M. Flagler and party leaving first train to arrive at Key West': panoramic photograph, 22 January 1912, Library of Congress, cut from its mount. Flagler was eighty-two; he died the next year.",
     (0.08, 0.385, 0.96, 0.648)),
    ("weather1935", "commons:Labor Day hurricane weather analysis (Enlarged), Sep 2, 1935.jpg",
     "The Weather Bureau's map, 2 September 1935", "weather",
     "Surface weather analysis for 2 September 1935, from the Monthly Weather Review, then published by the U.S. Weather Bureau: the storm as a closed low off the Florida Keys on the day it crossed them. A federal work."),
]


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA)).read()


def api(params):
    q = urllib.parse.urlencode({**params, "format": "json"})
    for wait in (0, 20, 60, 120):
        time.sleep(wait)
        try:
            return json.loads(get("https://commons.wikimedia.org/w/api.php?" + q))
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
    raise RuntimeError("Commons API still rate-limited")


def commons(fname, meta):
    page = next(iter(api({"action": "query", "titles": "File:" + fname, "prop": "revisions|imageinfo",
                          "rvprop": "content", "rvslots": "main", "iiprop": "url|size|extmetadata",
                          "iiurlwidth": 1600})["query"]["pages"].values()))
    text = page["revisions"][0]["slots"]["main"]["*"]
    lic = text[text.lower().find("license"):][:600] if "license" in text.lower() else text
    assert OK.search(text) and not BAD.search(lic), f"licence not PD/CC0: {fname}"
    ii = page["imageinfo"][0]
    if meta:
        em = ii.get("extmetadata", {})
        strip = lambda k: re.sub(r"<[^>]+>", "", em.get(k, {}).get("value", ""))[:200]
        print("   date:", strip("DateTimeOriginal"), "| author:", strip("Artist"), "| credit:", strip("Credit"),
              "| licence:", strip("LicenseShortName"))
    return ii.get("thumburl") or ii["url"], f"Wikimedia Commons, File:{fname} ({ii['descriptionurl']})"


def sciencebase(item, meta):
    d = json.loads(get(f"https://www.sciencebase.gov/catalog/item/{item}?format=json"))
    rights = str(d.get("rights") or "")
    assert "public domain" in rights.lower(), f"ScienceBase item not marked public domain: {item}"
    f = next(x for x in d["files"] if x["name"].lower().endswith(".jpg"))
    if meta:
        print("   title:", d.get("title"), "| rights:", rights[:90])
    return f["url"], f"U.S. Geological Survey Photographic Library, {f['name'].split('.')[0]}, ScienceBase item {item} (https://www.sciencebase.gov/catalog/item/{item}); U.S. public domain"


def archive(ref, meta):
    item, leaf = ref.rsplit(":", 1)
    md = json.loads(get(f"https://archive.org/metadata/{item}"))["metadata"]
    year = int(str(md.get("date", "9999"))[:4])
    assert year < 1931, f"archive.org item not before 1931: {item} ({md.get('date')})"
    if meta:
        print("   title:", md.get("title"), "| date:", md.get("date"))
    return (f"https://archive.org/download/{item}/page/n{leaf}_w2400.jpg",
            f"{md.get('title')} ({md.get('date')}), page image n{leaf}, archive.org {item} (https://archive.org/details/{item}/page/n{leaf}); published in the United States before 1931, public domain")


def main(meta=False):
    OUT.mkdir(parents=True, exist_ok=True)
    plates = []
    for pid, src, title, side, caption, *crop in PLATES:
        kind, ref = src.split(":", 1)
        url, source = {"commons": commons, "sciencebase": sciencebase, "archive": archive}[kind](ref, meta)
        dest = OUT / f"{pid}.jpg"
        if not dest.exists():
            im = Image.open(io.BytesIO(get(url))).convert("RGB")
            if crop:
                l, t, r, b = crop[0]
                im = im.crop((round(l * im.width), round(t * im.height), round(r * im.width), round(b * im.height)))
            if im.width > 1600:
                im = im.resize((1600, round(im.height * 1600 / im.width)))
            im.save(dest, "JPEG", quality=84, optimize=True)
            t = im.copy(); t.thumbnail((480, 480)); t.save(OUT / f"{pid}_t.jpg", "JPEG", quality=80)
            time.sleep(2)
        plates.append({"id": pid, "titel": title, "side": side, "caption": caption, "source": source})
        print(pid, dest.stat().st_size // 1024, "KB")
    (ROOT / "data" / "plates.json").write_text(json.dumps({"credit": CREDIT, "plates": plates}, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main("--meta" in sys.argv)
