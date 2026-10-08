"""Build data/storm1906.json, module 3: the quarterboats and the storm of October 1906.

Sources (public domain), each passage read against the page image:
- Monthly Weather Review 34:10 (October 1906), pp. 479–480: reports of the Weather Bureau's offices at Key West
  (F. E. Hartwell), Jupiter (H. P. Hardin) and Jacksonville (A. J. Mitchell) (archive.org
  sim_monthly-weather-review_1906-10_34_10, images n26–n27). A federal publication.
- Engineering News 56:17 (25 October 1906), p. 442: two notes, one with Vice-President J. R. Parrott's despatch
  to Flagler of 22 October (archive.org sim_enr_engineering-news-a-journ_1906-10-25_56_17, n19). The right
  edge of the column runs into the binding; letters lost there are supplied in square brackets.
- The Morning Oregonian (Portland), 22 October 1906, p. 4: Associated Press despatches from Key West, Savannah
  and Miami (Historic Oregon Newspapers, https://oregonnews.uoregon.edu/lccn/sn83025138/1906-10-22/ed-1/seq-4/).
- Frank M. Patterson, Railway Age Gazette 52:19 (10 May 1912), pp. 1040–1041 (archive.org
  sim_railway-age_1912-05-10_52_19, n11–n12).
- Monthly Weather Review 37:10 (October 1909), pp. 830–831 (archive.org sim_monthly-weather-review_1909-10_37_10,
  n133–n134). A federal publication.
Run from the repository root:  python tools/build-storm1906.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "storm1906.json"

MWR = "Mon. Weather Rev. 34 (1906), p. {}"
EN = "Eng. News 56 (1906), p. 442"
OR = "Morning Oregonian, 22 Oct. 1906, p. 4"
RAG = "Ry. Age Gazette 52 (1912), p. {}"
MWR9 = "Mon. Weather Rev. 37 (1909), p. {}"

SECTIONS = [
 {"id": "warning", "zk": "Warning", "titel": "The warning, 17 October 1906",
  "blurb": "The Weather Bureau ordered storm warnings for Key West before noon on 17 October; the hurricane crossed the keys in the night and the morning of the 18th. What the Bureau's observers said about the warnings, and what the railway's engineers said six years later.",
  "units": [
   (1, "Storm warnings ordered", MWR.format(479),
    "Storm warnings ordered and advices received 11:35 a. m., 17th. Wind gradually increased, and backed from east to northeast at 6 p. m., where it held until after midnight. Barometer fell steadily after 6 a. m., and at midnight stood at 29.45 inches. Up to midnight the wind velocity did not exceed 30 miles an hour. About 3:30 a. m., of the 18th, the wind backed to north, and by 4:30 a. m., to northwest. The barometer fell until 3 a. m., with minimum reading 29.30 inches. The center of the storm past very near and southeast of the station. At Sand Key the lowest reading was about 29.25 inches, and wind velocities as high as 75 miles an hour were recorded at that station. The highest velocity at Key West, 54 miles an hour, occurred at 7:20 a. m., of the 18th.",
    "The report of F. E. Hartwell, assistant observer of the Weather Bureau at Key West: the warning came some eighteen hours before the strongest wind."),
   (2, "Ample warnings", MWR.format(480),
    "It may be appropriate to say that ample warnings were issued in advance of the storm. Special messengers were sent to outlying points, and so far as possible thoro warning was given in Monroe, Dade, and the lower portion of Brevard counties, where the damage was greatest. At Miami many houses were blown down or damaged, and horticultural interests suffered much loss. The losses in and about Miami amounted to about $160,000. The loss of life among laborers extending the Florida East Coast Railway is placed at 124. The men lived in houseboats that were swept out to sea. The islands behind which the boats were anchored had afforded ample protection against previous storms. The stern-wheel steamer St. Lucie, used as a transport for the railway company, left Miami about noon of the 17th. The northeast storm warning was flying at that time and messages from the Central Office urged vessels to remain in port. The St. Lucie was lost and many of her passengers were drowned, but it may be well to state that the master of the vessel left port without consulting the proper officials of the railway, who always direct that proper precaution be taken on the Weather Bureau warnings.",
    "A. J. Mitchell, observer at Jacksonville. He defends the Bureau's warnings and, in the same report, the railway: the master of the St. Lucie left 'without consulting the proper officials'. Of the men on the houseboats he says only that the islands had protected them before."),
   (3, "A wholesome fear", RAG.format(1040),
    "Reference having been made to the hurricanes, it may be of interest to review their connection with the work. These storms, arising in the West Indies and resembling the East Indian typhoons, may be looked for in August, September and October, but are most apt to occur in the latter month. The greatest loss of life and damage to equipment from this cause occurred in 1906, although that storm was not so severe as those of 1909 and 1910. A hurricane was predicted in 1905, the year the work was started, and strict orders were given by the constructing engineer to prepare for it. It is perhaps unfortunate that the predictions that year did not materialize into a moderately severe blow, for there were fewer men on the work then and a wholesome fear would have been instilled in all. In 1906 when warnings were again issued they were not given much attention except where the constructing engineer and his principal assistant could see personally that they were observed.",
    "Patterson wrote six years later, from the railway's records and its engineers. Who did not heed the warnings, the men or the foremen and engineers in charge of the boats, he does not say."),
  ]},
 {"id": "boat", "zk": "Houseboat No. 4", "titel": "Houseboat No. 4",
  "blurb": "The survivors' account, as the Associated Press sent it from Key West, Savannah and Miami and the Morning Oregonian printed it on 22 October 1906: the houseboat at Long Key with about 150 men, the night at sea, and the steamers that picked men off the wreckage.",
  "units": [
   (4, "Five o'clock Thursday morning", OR,
    "KEY WEST, Fla., Oct. 22.—Survivors from one of the houseboats on the Florida East Coast Railway extension along the Keys tell a harrowing tale of death and destruction caused by the storm of Thursday. W. P. Dusenberry, civil engineer in charge of the work on Long Key, arrived here on the Russian steamer Jennie, among other survivors rescued. He says houseboat No. 4, on which were 150 men, was struck by the storm at 5 o'clock Thursday morning and was driven out into the gulf. At 6 o'clock the houseboat began to break up and as the great waves hit her, men, singly and in bunches of two and three, were washed into the sea and drowned.",
    "Thursday was 18 October. The engineer's name is spelled Dusenberry here and in Parrott's despatch ([10])."),
   (5, "Crushed to death in the collapse", OR,
    "Some went below for protection, but when the top of the boat was carried away, the waves rushed in and the boat soon went to pieces, 39 or 40 of the men being crushed to death in the collapse, the others grabbing timbers to save themselves from drowning. Dusenberry was in the hold, but succeeded in getting on to a log and floated until Friday night. On one piece of timber 16 men were clinging and nine were hanging to another. The sides of the houseboat were crowded with men. It turned over three times, each time reducing the number. The steamer Jennie sighted the wreckage and succeeded in rescuing the 99 men who were brought here. Three other steamers were picking up dead and alive men when the Jennie left the scene.",
    "The Weather Bureau's office at Key West reported 49 men brought in by the Jenny ([8]); this despatch gives 99."),
   (6, "Ten boats at Long Key", OR,
    "There was another houseboat with 150 men on board at Long Key, which Mr. Dusenberry thinks was also swept to sea. There were in all ten boats at Long Key, mortar mixers, dredger and other boats engaged in the work. The survivors were furnished food and clothing from the East Coast Railway commissary here and were given medical attention.",
    None),
   (7, "Bruised and torn", OR,
    "SAVANNAH, Ga., Oct. 21.—The British steamer Alton, Captain Bell, arrived in this port with 24 survivors of houseboat No. 4, which was engaged in building the extension of the Florida East Coast Railroad to Key West. The survivors were picked up Thursday. The Alton had passed just in time and had seen the signals of distress. The rescued were bruised and torn in their efforts to keep their hold on the wreckage, to which they had clung after the houseboat went to pieces. There were 1[3]7 men on the houseboat at the time. It is believed that at least 20 lost their lives.",
    "The second digit of the number of men aboard is blurred in the scan: 137 or 177. The Key West despatch gives 150 ([4]), Parrott's despatch 104 ([10])."),
   (8, "Spare no expense", OR,
    "MIAMI, Fla., Oct. 21.—Reports from Long Key are that every house was demolished by Thursday's storm and it was there that so many of the men employed on the Florida East Coast Railway extension lost their lives. Damage to the roadbed and concrete viaducts of the extension was very light and there will be no delay in construction. All the injured are in the hospital here receiving the best of medical attention. Henry M. Flagler telegraphed from New York to spare no expense in caring for the men and their families. Only a few of the men were dangerously injured, most of them suffering merely from sprains, bruises, abrasions and exposure.",
    None),
  ]},
 {"id": "count", "zk": "Count", "titel": "Counting the dead",
  "blurb": "Every source gives a different number. The Weather Bureau's three offices gave three in one article; the railway's vice-president counted the missing; the engineering press six years later gave a lower figure, and the Weather Bureau three years later a far higher one. No list of the dead has been found.",
  "units": [
   (9, "Probably more than 100", MWR.format(479),
    "Every effort was made to give the warnings the widest possible circulation, and little damage was done on the island. Among the small boats in the harbor those taking precautions escaped, but others suffered considerable damage, and some were destroyed by pounding against the docks. The Revenue cutter Fessenden was the only large vessel that received injury in this port. The Mallory steamer Concho remained in port about forty-eight hours, and the Peninsula and Occidental steamers Mascotte and Miami were held for a considerable time. The progress of the storm up to the keys was marked by very high water, which, with the wind, caused much destruction of property. The quarter boats of the East Coast Extension were carried out to sea and many lives, probably more than 100, were lost. Forty-nine men were picked up by the Austrian steamer Jenny and returned to Key West, 24 were landed at Savannah, Ga., and a number were picked up by other steamers.",
    "The Weather Bureau at Key West. The rescuing steamer is Austrian here, Russian in the Associated Press despatch ([4]) and Italian in Parrott's ([10])."),
   (10, "146 missing", EN,
    "THE SOUTHERN STORM LOSS to the Florida East Coast Ry. was comparatively light so far as damage to the line of road under construction is concerned. According to a despatch dated Oct. 22, from St. Augustine, Fla., from Vice-President J. R. Parrott to President H. M. Flagler, 26 Broadway, New York, all finished piers and equipment at Key West are safe; the partly finished work, however, is gone. The water did not go acro[ss] the finished grade at any point. Some exposed ro[ck] embankment was slightly damaged, and the earth em[-]bankment was badly washed in places. At Big Pine K[ey] the water tanks and excavator are intact, but t[he] tentage and supplies are all gone. Several lighters we[re] sunk at Knights Key, but most of the cargo was sav[ed]. At Long Key the entire equipment is gone except o[ne] excavator, one barge, a steam lighter stout, one quar[ter-]boat and one launch. At Lower Matecumbe 45 men [are] missing from two house-boats used for caring for dre[dge] crews. Three house-boats and three dredges were slig[htly] damaged, but the crews were saved. A pile driver, how[-]ever, was lost with two men aboard. Besides 20 m[en] lost on the \"St. Lucie,\" there are 146 missing. A qua[r-]terboat with 104 men aboard broke up after cross[ing] the outer reef at Long Key. Of these, Engineer Du[sen-]berry and 48 men were picked up by an Italian st[eamer] and carried to Key West; in addition, 23 men fro[m the] quarterboat were later brought into port.",
    "The railway's own count, four days after the storm, reported first as damage to the line. Letters lost where the column runs into the binding of the scanned volume are supplied in square brackets; the word '[are]' is a conjecture."),
   (11, "Ten barges, 150 men each", EN,
    "A CYCLONIC STORM, which swept over Cuba Oct. 1[8], reached as far north as the Carolinas, doing great [dam-]age, especially on the East Coast of Florida. The pro[p-]erty loss at Havana, Cuba, is estimated at $2,000,[000], while some 20 Cubans were killed. Ten barge[s], each carrying 150 men employed by the Florida East Coa[st Ry.] on its extension from Miami to Key West, Fla., were carried out to sea, and up to the present time only part of these laborers have been accounted for.",
    "A second note in the same column of the same issue, from another source: ten barges of 150 men each would be 1,500 men."),
   (12, "About 135", MWR.format(479),
    "No damage resulted in this vicinity, as the warnings had caused measures of protection to life and property before the storm reached here. At the extreme southern end of the State where the Florida East Coast Railway Company is building its line over the keys and water into Key West, the company's property loss was about $200,000. Planters on the larger keys lost their orange groves, pineapple fields, and homes, and in some cases the losses were so complete that the places have been abandoned. Six lives are reported to have been lost on plantations thus destroyed. The storm caught most of the several hundred laborers and mechanics of the railway extension on houseboats and other clumsy craft moored to piling for living quarters. These boats were torn from their moorings and beaten to pieces by the seas. The loss of life among these men was about 135. One hundred and fifty men were picked up at sea on wreckage by steamers bound in and out of the Gulf. One passenger steamer, the St. Lucie, an old river packet, was swamped and 23 of the 80 people on board were lost near Elliotts Key.",
    "H. P. Hardin, observer at Jupiter. With [2] (124) and [9] (more than 100) the same article of the Monthly Weather Review gives three figures."),
   (13, "Over 70 men were lost", RAG.format("1040–1041"),
    "As a consequence when the storm broke it found the greater part of the men and equipment helpless, or worse than helpless, for most of the laborers were housed in quarterboats and had taken refuge in them. These boats were soon blown out to sea, over 70 men were lost and many others were picked up by passing steamers after days of suffering.",
    "The lowest figure in the sources, written for railway officers in the year of the opening."),
   (14, "Many hundreds", MWR9.format("830–831"),
    "The correctness of the warning and the effectiveness of its distribution are indicated in the small loss of life, about one dozen, along the lines of the projected railroad. Those who were drowned paid the penalty of remaining aboard a tugboat, which sank, instead of seeking shelter, as others did. With about 3,000 laborers scattered many miles over the low islands of the sea along the proposed route of the Florida East Coast Railroad the fact that the loss of life was so small is an eloquent tribute to the wisdom of the railroad officials in obeying implicitly the information given out by the Weather Bureau. In 1906 many hundreds of laborers were drowned during a tropical storm as a consequence of ignoring warnings.",
    "The same observer at Jacksonville, A. J. Mitchell, on the storm of October 1909, three years after his report of 1906 ([2]) put the dead at 124. The highest figure in the sources, written to show what warnings were worth (module 5)."),
  ]},
 {"id": "after", "zk": "After", "titel": "After 1906",
  "blurb": "What changed. The railway's account of the precautions taken from 1906 on, against which the storms of 1909 and 1910 were measured.",
  "units": [
   (15, "A barometer in every camp", RAG.format(1041),
    "Since 1906 every precaution has been taken to protect lives and property when information of an impending hurricane is received. Each engineer's camp is provided with a barometer and the weather bureau at Washington has given valuable aid and sends warnings promptly whenever it gets reports of an approaching storm. At such times the land equipment is put in shape to stand the storm as best it may, the floating equipment is taken to sheltered places and sunk in shallow water and the men are assembled at such places as will afford the best protection. It is worthy of note that the storms of 1909 and 1910, the most severe known on the coast of Florida, caused little loss of life and equipment.",
    "The floating equipment was sunk in shallow water to save it; where the men were assembled Patterson does not say. In 1909 about a dozen men drowned aboard a tugboat ([14]; module 5)."),
  ]},
]

COMPARE = [
 {"id": "dead1906", "titel": "How many died in October 1906?",
  "frage": "More than 100, about 135, 124, 146 missing, over 70, or many hundreds?",
  "note": "The figures come from the Weather Bureau's offices at Key West, Jupiter and Jacksonville in the same article of 1906, from the railway's vice-president four days after the storm, from the railway trade press in 1912 and from the Weather Bureau's Jacksonville observer in 1909. They count different things (the dead, the missing, the men of one boat or of all), at different times, for different readers. No list of names has been found. The apparatus gives each figure and does not choose.",
  "voices": [{"text": "storm1906", "sec": "count", "n": [9, 12]},
             {"text": "storm1906", "sec": "count", "n": [10]},
             {"text": "storm1906", "sec": "count", "n": [13, 14]}]},
 {"id": "blame1906", "titel": "Who ignored the warnings?",
  "frage": "The master of the St. Lucie, the men on the houseboats, or the railway?",
  "note": "In 1906 the Weather Bureau's Jacksonville observer stressed that the warnings were ample and that the master of the St. Lucie had sailed without consulting the railway. In 1909 the same observer wrote that in 1906 'many hundreds' had drowned 'as a consequence of ignoring warnings'. The railway's account of 1912 says the warnings were not given much attention except where the two chief engineers could see to it themselves. None of them says who decided that the men should stay on the boats.",
  "voices": [{"text": "storm1906", "sec": "warning", "n": [2]},
             {"text": "storm1906", "sec": "warning", "n": [3]},
             {"text": "storm1906", "sec": "count", "n": [14]}]},
]


def main():
    sections = []
    for s in SECTIONS:
        units = []
        for n, titel, pg, en, note in s["units"]:
            u = {"n": n, "pg": pg, "titel": titel, "en": en}
            if note:
                u["note"] = note
            units.append(u)
        sections.append({k: s[k] for k in ("id", "zk", "titel", "blurb")} | {"units": units})
    data = {
        "titel": "The quarterboats and the storm of October 1906",
        "autor": "The Weather Bureau's observers at Key West, Jupiter and Jacksonville (Monthly Weather Review, 1906 and 1909); Engineering News (1906) with J. R. Parrott's despatch; the Associated Press in the Morning Oregonian (1906); Frank M. Patterson in the Railway Age Gazette (1912)",
        "jahr": "1906–1912",
        "quelle": "Monthly Weather Review 34:10 (Oct. 1906), pp. 479–480 (archive.org sim_monthly-weather-review_1906-10_34_10); Engineering News 56:17 (25 Oct. 1906), p. 442 (archive.org sim_enr_engineering-news-a-journ_1906-10-25_56_17); The Morning Oregonian, 22 Oct. 1906, p. 4 (Historic Oregon Newspapers, University of Oregon, https://oregonnews.uoregon.edu/lccn/sn83025138/1906-10-22/ed-1/seq-4/); Frank M. Patterson, \"The Florida East Coast Extension,\" Railway Age Gazette 52:19 (10 May 1912), pp. 1040–1041 (archive.org sim_railway-age_1912-05-10_52_19); Monthly Weather Review 37:10 (Oct. 1909), pp. 830–831 (archive.org sim_monthly-weather-review_1909-10_37_10). All public domain: the Monthly Weather Review is a federal publication, the others were published in the United States before 1931.",
        "hinweis": "Every passage was read against the page image. The column of Engineering News of 25 October 1906 runs into the binding of the scanned volume: letters lost there are supplied in square brackets, conjectures marked. In the Oregonian the number of men aboard in the Savannah despatch is blurred and given as 1[3]7. The workers do not speak here except through the survivors' account passed on by an engineer and a news agency; no name of a drowned worker has been found in these sources.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    cmp_path = ROOT / "data" / "compare.json"
    cmp = json.loads(cmp_path.read_text(encoding="utf-8"))
    cmp["pairs"] = [p for p in cmp.get("pairs", []) if p["id"] not in {c["id"] for c in COMPARE}] + COMPARE
    cmp_path.write_text(json.dumps(cmp, ensure_ascii=False, indent=1), encoding="utf-8")
    print(OUT.name, sum(len(s["units"]) for s in sections), "passages in", len(sections), "sections;", len(cmp["pairs"]), "comparisons")


if __name__ == "__main__":
    main()
