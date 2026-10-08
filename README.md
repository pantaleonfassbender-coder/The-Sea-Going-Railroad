# The Sea-Going Railroad

A documentary apparatus for the Florida East Coast Railway's extension across the Florida Keys to Key West: its building from 1905 to 1912, the hurricanes of 1906, 1909 and 1910, the recruiting of its labour and the peonage trial of 1908, its years of running at a loss, the Labor Day hurricane of 2 September 1935, and the Overseas Highway built on its piers in 1938.

Its question is who carried the risk of the work: the men on the quarterboats, the recruits whose fare was deducted from their wages, the company that never made the line pay, and the war veterans in the relief camps on the keys in 1935.

Live: https://the-sea-going-railroad.netlify.app/

**Stage 1 is in progress (October 2026).** Six modules are carried: *The plan and the first year, 1904–1906* (28 passages: Scientific American 1905, the Railroad Gazette 1905 and 1906, the railway's booklet of 1912) *Arches or fill: how the line was built, 1905–1912* (24 passages: Carver and Venable in the Engineering Record 1906 and 1907, Thacher to the Engineering Association of the South 1911, Patterson in the Railway Age Gazette 1912) and *The quarterboats and the storm of October 1906* (15 passages: the Monthly Weather Review 1906 and 1909, Engineering News 1906, the Associated Press in the Morning Oregonian, Patterson 1912; with two comparisons) and *Recruited in New York: wages, deductions, the chain gang and the peonage trial* (17 passages: Spooner 1907, Thacher 1911, Patterson 1912, the Associated Press 1908, the Immigration Commission 1911) and *1909, 1910, and Key West, 22 January 1912* (15 passages: the Monthly Weather Review 1909 and 1910, the Engineering Record 1910, Patterson 1912, Pope 1912) and *Running at a loss, 1912–1935* (11 passages: Patterson 1912, the Interstate Commerce Commission 1936 and 1939). One more is planned: 2 September 1935, with the end of the line.

Sources are public domain only: the American engineering press and the railway's publications before 1931, and works of the United States government (Monthly Weather Review, Reports of the Immigration Commission, the House hearings *Florida Hurricane Disaster* of 1936, decisions of the Interstate Commerce Commission, the National Park Service). Figures are given as each source gives them; where the sources disagree, the apparatus says so. Photographs of the dead of 1935 are not shown.

The companion game, *An Act of God* (in preparation): https://github.com/pantaleonfassbender-coder/An-Act-of-God

## Files

- `data/modules.json`: the modules carried and planned, and what is not carried and why.
- `data/plan.json`, `data/arches.json`, `data/storm1906.json`, `data/labour.json`, `data/storms1909.json`, `data/loss.json`: modules 1 to 6, built by the matching `tools/build-*.py` (`build-storm1906.py`, `build-labour.py` and `build-loss.py` also write their comparisons), which carry the transcriptions and their page references.
- `data/timeline.json`, `data/compare.json`, `data/plates.json`.
- `tools/make-plates.py`: fetches the plates from Wikimedia Commons, the USGS ScienceBase and archive.org scans after checking that each is in the public domain.

## Running locally

Any static server, e.g. `python -m http.server 8970`.

Code: MIT. Editions of public-domain texts: CC0. Editorial matter: CC BY 4.0. See `LICENSES.md`.
