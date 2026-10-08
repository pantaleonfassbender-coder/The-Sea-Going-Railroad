# The Sea-Going Railroad

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23245854.svg)](https://doi.org/10.5281/zenodo.23245854)

A documentary apparatus for the Florida East Coast Railway's extension across the Florida Keys to Key West: its building from 1905 to 1912, the hurricanes of 1906, 1909 and 1910, the recruiting of its labour and the peonage trial of 1908, its years of running at a loss, the Labor Day hurricane of 2 September 1935, and the Overseas Highway built on its piers in 1938.

Its question is who carried the risk of the work: the men on the quarterboats, the recruits whose fare was deducted from their wages, the company that never made the line pay, and the war veterans in the relief camps on the keys in 1935. The title is that of Chester C. Pope's account of the opening (1912).

Live: https://the-sea-going-railroad.netlify.app/

**Stage 1 is closed (October 2026).** It carries seven modules with 133 passages, each read against the page image of a public-domain printing:

- **The plan and the first year, 1904–1906** (28 passages) — Scientific American (1905); The Railroad Gazette (1905; Harry C. Smith 1906); the railway's booklet for the opening (1912).
- **Arches or fill: how the line was built, 1905–1912** (24) — George P. Carver and William Mayo Venable in The Engineering Record (1906, 1907); L. M. Thacher to the Engineering Association of the South (1911); Frank M. Patterson in the Railway Age Gazette (1912).
- **The quarterboats and the storm of October 1906** (15) — the Monthly Weather Review (1906, 1909); Engineering News with J. R. Parrott's despatch (1906); the Associated Press in the Morning Oregonian (1906); Patterson (1912).
- **Recruited in New York: wages, deductions, the chain gang and the peonage trial** (17) — F. E. Spooner in The Railroad Gazette (1907); Thacher (1911); Patterson (1912); the Associated Press on the trial of November 1908; the Reports of the Immigration Commission (1911).
- **1909, 1910, and Key West, 22 January 1912** (15) — the Monthly Weather Review (1909, 1910); The Engineering Record (1910); Patterson (1912); Chester C. Pope, "The Sea-Going Railroad" (1912).
- **Running at a loss, 1912–1935** (11) — Patterson (1912); the Interstate Commerce Commission (217 I.C.C. 325, 1936; 235 I.C.C. 211, 1939).
- **2 September 1935: the veterans, the train, and "an act of God"** (23) — the Monthly Weather Review (1935); the House hearings *Florida Hurricane Disaster* (1936), with the report to the President of 8 September 1935, the railway's letters and statements and the count of the dead; the Interstate Commerce Commission (1936); the National Park Service (1938).

A **Compare** page sets the sources side by side on six questions (the dead of 1906, the warnings of 1906, whether the men were held against their will, whether the line paid, whether the men of 1935 could have been saved, the dead of 1935). A **timeline** of nineteen stations links into the texts; fifteen public-domain **plates** are named with their originals.

Figures are given as each source gives them; where the sources disagree, the apparatus says so and does not choose. The workers speak in these sources only through others. Photographs of the dead of 1935 are not shown. What is **not carried**, and why, is listed on the Texts page (`data/modules.json`, key `missing`).

The companion game, *An Act of God* (in preparation): https://an-act-of-god.netlify.app/

## Files

- `data/modules.json`: the modules carried, and what is not carried and why.
- `data/plan.json`, `data/arches.json`, `data/storm1906.json`, `data/labour.json`, `data/storms1909.json`, `data/loss.json`, `data/act.json`: the seven modules, built by the matching `tools/build-*.py`, which carry the transcriptions and their page references (`build-storm1906.py`, `build-labour.py`, `build-loss.py` and `build-act.py` also write `data/compare.json`).
- `data/timeline.json`, `data/compare.json`, `data/plates.json`.
- `tools/make-plates.py`: fetches the plates from Wikimedia Commons, the USGS ScienceBase and archive.org scans after checking that each is in the public domain.

## Building the data

```
python tools/build-plan.py
python tools/build-arches.py
python tools/build-storm1906.py
python tools/build-labour.py
python tools/build-storms1909.py
python tools/build-loss.py
python tools/build-act.py
python tools/make-plates.py
```

## Running locally

Any static server, e.g. `python -m http.server 8970`.

## Citation

Fassbender, Pantaleon. *The Sea-Going Railroad: A Documentary Apparatus.* 2026. https://doi.org/10.5281/zenodo.23245854 (all versions; version 1.0.0: https://doi.org/10.5281/zenodo.23245855). Please also cite the printed source of any passage you quote. Metadata: `CITATION.cff`, `.zenodo.json`.

Code: MIT. Editions of public-domain texts: CC0. Editorial matter: CC BY 4.0. See `LICENSES.md`.
