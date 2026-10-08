"""Build data/labour.json, module 4: recruited in New York; wages, deductions, the chain gang and the peonage trial.

Sources (public domain), each passage read against the page image:
- F. E. Spooner, "Building the Florida East Coast Extension to Key West," The Railroad Gazette 42:17
  (26 April 1907), pp. 583–584 (archive.org sim_railway-age_1907-04-26_42_17, images n16–n17).
- L. M. Thacher, "Key West Extension of the F. E. C. Ry.," Engineering Association of the South, vol. XXII
  (1911), p. 72 (Google scan in https://historicbridges.org/florida/sevenmilebridge/articles.pdf, PDF p. 40).
- Frank M. Patterson, "The Florida East Coast Extension," Railway Age Gazette 52:19 (10 May 1912), p. 1041
  (archive.org sim_railway-age_1912-05-10_52_19, n12).
- Associated Press, New York, 13 November 1908, in The Paducah Evening Sun (Kentucky), 14 November 1908, image 10
  (Library of Congress, Chronicling America, batch kyu_nirvana, sn85052114; read in the IIIF page image).
- Reports of the Immigration Commission: Abstracts of Reports, vol. 2 (61st Cong., 3d sess., S. Doc. 747, 1911),
  pp. 439, 445–446 (archive.org abstractsreport01benngoog, n454, n456–n457). A federal publication.
Smith's report of 1906 on the first camps, the strike at Key West and the complaints is carried in module 1.
Run from the repository root:  python tools/build-labour.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "labour.json"

SP = "R.R. Gazette 42 (1907), p. {}"
TH = "Eng. Assoc. South XXII (1911), p. 72"
RAG = "Ry. Age Gazette 52 (1912), p. 1041"
AP = "Paducah Evening Sun, 14 Nov. 1908"
IC = "Immigration Comm., Abstracts II (1911), p. {}"

SECTIONS = [
 {"id": "recruits", "zk": "Recruits", "titel": "Recruited in the North",
  "blurb": "Where the men came from and how the railway's engineers and the trade press described them: Black workers from Florida first, then thousands of men sent from New York, Philadelphia and Boston by agencies, later Spaniards by way of Cuba. Three accounts written for engineers and railway officers, 1907 to 1912.",
  "units": [
   (1, "As tough a crowd", SP.format(583),
    "Years ago, when surveyors first went over the Keys to determine the practicability of this extension, while climbing through the thick undergrowth they were almost eaten alive with mosquitoes and terribly poisoned by poison ivy and other poisonous plants. Then 150 negroes were taken on to clear the way. Later, when grading was begun at the Homestead camp, white men came as laborers, and since that time the number has been steadily increased. A carte blanche order for men to employment agencies to New York brought out about as tough a crowd as were ever got together. Later the agencies were given up and men went north to recruit, but with little better results; nor are the men who are going to the work to-day of much better class. Nevertheless, although in the ranks to-day may be found jail birds, tramps and election repeaters, the men have straightened up and are doing good work. This is largely because they have no chance to get liquor anywhere.",
    "Spooner spent three weeks on the work in the spring of 1907 and wrote, as he says, in view of the newspaper stories of peonage. His view of the men is his own."),
   (2, "Ten thousand men", TH,
    "As many camps as possible were opened with negro labor; but the supply was short, and recourse was had to white labor from the North and obtained mostly at New York and Philadelphia. Some 10,000 men were obtained in this way, though not more than 5,000 or 6,000 were at work at any one time. A great deal of care was taken in the selection of these men by the agents, but in spite of this a great many poor and worthless hands were obtained. Transportation was furnished each man, which was charged against him, and he was allowed to pay it back in small installments at his convenience. This labor was made up of all classes, from the clerk out of work to the worthless bum who did not intend to work, and even criminals.",
    "Thacher says the supply of Black labour was short; Patterson ([3]) says it was considered and found 'insufficient and inefficient'. Both are the railway's engineers."),
   (3, "The labor question", RAG,
    "The question of labor has been a serious one and was particularly troublesome in the early stages of the work. The use of negroes recruited from Florida and neighboring states was considered, but the supply was found to be insufficient and inefficient on this class of work. Italian and Greek labor was tried and found wanting, and arrangements were made for securing common labor in New York through labor agencies established by the railway. In spite of the care taken to select only men fitted for the work, much trouble was experienced at first with incompetents and with those who recruited with no idea other than to secure a trip to Florida at the expense of the company.",
    "The railway's judgements of 1912 on whole groups of workers, quoted as printed. Smith found Black workers clearing the jungle in camps of their own in 1906 (module 1 [14])."),
   (4, "Industrious, intelligent and sober", RAG,
    "During the last few years Spanish labor has been used in increasing numbers, until at the present time this class constitutes from 20 to 25 per cent. of the entire force. This labor has proved most efficient, being industrious, intelligent and sober. The Spaniards are used principally as common laborers, though many have shown themselves capable of a higher class of work, and have been used as firemen, calkers and stationary engineers.",
    "The company's booklet of 1912 says the Spaniards came 'by way of Cuba, from the northern provinces of Spain' (module 1 [23])."),
  ]},
 {"id": "terms", "zk": "Terms", "titel": "Wages, fare and deductions, 1907",
  "blurb": "What a man was paid, what was deducted, where he slept and how he could leave: Spooner's account of April 1907, the most detailed in the sources.",
  "units": [
   (5, "Thirty-five to forty-five dollars", SP.format(583),
    "The men are willing to have this rule enforced, for they have a chance to save money. Ordinary laborers get from $35 to $45 a month; sub-foremen or gang foremen, $60, and foremen $90 a month. Engineers are paid from $175 a month up. All have their board and lodging free. The colored men live in tents and have their cooking done by colored women, supplies being furnished from the railroad commissary. The white men generally live in what are known as quarter houses, which are hotels on boats with bunks banked one above the other. The bunks, windows and doors are screened with mosquito netting.",
    "The rule is the ban on liquor ([1]). Black workers in tents on land, white workers on the boats: the separation Smith saw in 1906 (module 1 [14]). In October 1906 the boats were where the men drowned (module 3)."),
   (6, "Ten dollars fare", SP.format(583),
    "As already mentioned, the men are secured for the most part in the large cities of the North, particularly New York, Philadelphia and Boston. They are shipped to Florida by boat with their fare paid. This fare, $10, and $2 for board on the way, is charged against their account and deducted from the wages due them, usually at the end of the first month. Of the men who start south about one-fourth desert on the way and never reach the work. Of those who do arrive, many are unfit to work, in which case they are sent to the hospital at Miami, where they receive treatment without expense. This hospital is maintained by the company, its only source of income being the fares of the men who are returning home, and who pay $1.50 for transportation from the Keys to Miami. Over 4,000 cases have been treated in this hospital, of which not 10 per cent. represented diseases indigenous to Florida.",
    "By Spooner's account a man who left before his first pay day had not yet paid off the twelve dollars. The figures in this passage (wages, fare, the quarter who deserted) are those the companion game uses."),
   (7, "Thirty dollars a month saved", SP.format(583),
    "In the camps the only chance to spend money is at the commissary, where certain luxuries, not including liquor, may be obtained. The commissaries are run by a Miami grocer named Lumis, whose profit is limited to an average of 15 per cent. on his sales. Most of the men keep bank accounts with the engineer in charge of their camp, who holds funds subject to their order. Many laborers save as much as $30 a month.",
    "The men's savings were held by the engineer in charge of their camp."),
   (8, "Out of sight of the mainland", TH,
    "Those who came with the idea of escaping the cold weather North and living in a climate where the sunny skies would afford them all kinds of tropical fruits, without the trouble of working for them, were, of course, disappointed. These disgruntled men wrote to the Northern papers all sorts of harrowing tales regarding their hardships under cruel and remorseless taskmasters—how they were hounded by foremen with guns and driven to work under the lash. As a matter of fact, it is very doubtful if in the whole lot any one was ill treated, at least none within the writer's knowledge. Of course the men were more isolated and cut off from civilization than miners in the Black Hills of Dakota fifty years ago, as most of the Keys are out of sight of the mainland, with no way to reach it except by the boats of the company. The men had tents furnished them, and good, substantial food at a nominal cost, or they could board themselves from the commissary, as they chose. For any who really desired to make money and save it the situation was admirable, as there was absolutely no way to spend it, except by going to Miami or Key West.",
    "Thacher: no ill-treatment 'within the writer's knowledge', and no way off the keys except by the company's boats."),
  ]},
 {"id": "chain", "zk": "Chain gang", "titel": "The chain gang",
  "blurb": "The company's answer to the stories of peonage: the men who told them had deserted before reaching the work and been sentenced as vagrants in Jacksonville or Miami. The explanation describes forced labour of its own, under Florida's vagrancy laws.",
  "units": [
   (9, "Guns and dogs", SP.format(583),
    "Apparently the stories of peonage can be traced to the following set of circumstances: Men start for the South to work on the extension but desert, go to Jacksonville or Miami, and, having little or no money and no desire to work, are sooner or later arrested as vagrants and put into the chain gang, where they have a man with a gun to watch them and dogs to chase them if they try to get away. When they are released they go north and tell harrowing tales of being guarded by guns and dogs, after going to Florida to work on the extension. What they say about being made to work is true, but they never reached the Florida East Coast extension at all.",
    "Spooner does not dispute the guns, the dogs or the forced work, only where they happened. His own account shows how close the two were: a man who left the work without money could be arrested as a vagrant. The Immigration Commission in 1909 questioned prisoners of the chain gang on the streets of Miami ([15]); Smith saw men from the strike at Key West serving terms as vagrants in 1906 (module 1 [18])."),
   (10, "\"All he has to do\"", SP.format("583–584"),
    "One of the first \"peons\" seen was carefully questioned about peonage, to his great amusement. \"The job's all right,\" he said, \"and I never saw a man who could not leave any time he wanted to, even though he did not have the price, nor yet have worked off his fare from the North. All he has to do to get away is to refuse to work.\" Another man told of some of his comrades who, wishing to return to work after leaving, missed a packet boat and hired a launch to get back. Of course, men get tired of the life and want a change, and in such circumstances they are encouraged to leave, but are told that their place is waiting for them if they wish to return and half of them come back. Men have gone back to New York and returned bringing others with them.",
    "The only worker quoted in the trade press, unnamed, questioned by a visitor travelling with the railway's engineers. 'Refuse to work' is also what the prosecution said led to beatings ([12])."),
  ]},
 {"id": "trial", "zk": "Trial", "titel": "The trial, New York, November 1908",
  "blurb": "In November 1908 four employees and agents of the railway were tried in the federal circuit court at New York for peonage and slavery. The prosecution's case as the Associated Press reported it on the first day, and the outcome as the railway press reported it four years later.",
  "units": [
   (11, "The practical marooning of 3,000 men", AP,
    "New York, Nov. 13.—What was asserted to be the practical marooning of 3,000 men in the wild regions of Florida and their detention there under hard labor for a period of several months was dealt with at length today before Judge Hough and a jury in the United States circuit court, in the course of the trial of the government's case against employes and agents of the Florida East Coast Railway company for alleged violation of the statute prohibiting \"peonage, slavery and enforced servitude.\" The men under indictment are Francisco Sabbia, Edward J. Triay, David E. Harley and Frank A. Hough. After a jury had been selected, Deputy Attorney General Glenn E. Usted outlined the prosecution's case, contending that the treatment accorded the workmen supplied to the Florida East Coast company by the defendants was nothing short of slavery. The government would show, he declared, that in 1905 the men had been induced by alluring advertisements to apply for employment in the south.",
    "The prosecutor's name is printed 'Usted' throughout; the spelling has not been checked against another report. The despatch gives the prosecution's assertions on the first day of the trial, not findings."),
   (12, "A hose was turned on them", AP,
    "Everything went well, the attorney said, until the men reached Jersey City, where they were put aboard a train, the doors being locked on them and armed guards set over them to prevent their escape. Throughout the long journey they were given nothing but stale bread and bologna sausage, and when they reached the end of their journey many rebelled and refused to leave the train, but a hose was turned on them, and in this manner the entire consignment of human freight had been driven aboard a waiting steamer. When the ultimate destination was reached, said Mr. Usted, the men found that the paradise that had been promised them was a barren wilderness, overrun with reptiles and venomous snakes, where no place to sleep had been provided for them. Their \"high wages,\" the prosecutor declared were slips of paper exchangeable at the company's store for shoes and clothing and food. The escape that many sought was impossible, as the region was entirely cut off from all means of communication with the outside world. Thinking to be discharged, some refused to work. These, Mr. Usted said, were threatened with death and brutally beaten. Finally some were able to smuggle letters through to relatives, and in this manner the government had been apprised of the conditions existing.",
    "Against this: Spooner's man who could leave 'any time he wanted to' ([10]) and Thacher's 'very doubtful if … any one was ill treated' ([8]). Thacher too says there was no way off the keys but the company's boats."),
   (13, "One charge destroyed the other", AP,
    "John B. Stanchfield, attorney for the Florida East Coast company, and personal counsel for Henry M. Flagler, the company's president and principal stockholder, moved that the indictments charging peonage and slavery be dismissed, as the one charge destroyed the other. Judge Hough was inclined to hold that the charge of peonage could not rest, but declared that he would rule in the matter on any point brought out during the presentation of the evidence.",
    "Peonage under the federal statute meant holding a man to work off a debt; the Immigration Commission explains why other forms of forced labour could hardly be punished ([16])."),
   (14, "A verdict of not guilty", RAG,
    "Out of this grew the peonage charges which resulted in federal indictment of the engineers in charge and their New York agent. These charges received highly sensational treatment in the press, but when, after hard fighting, the railway was able to bring the cases to trial, the result was a verdict of acquittal. No evidence was presented by the defense and the court directed a verdict of \"not guilty,\" at the same time rebuking the prosecuting attorney for wasting its time with a charge which had so flimsy a foundation.",
    "The railway's account, four years later. The date of the verdict and the court's words have not yet been found in a contemporary report; the national newspaper archive could not be searched from here."),
  ]},
 {"id": "commission", "zk": "Commission", "titel": "The Immigration Commission, 1909–1911",
  "blurb": "In March 1908 the House of Representatives asked the Immigration Commission to look into, among others, the railway camps of Florida. Its report of 1911 on the Florida East Coast case, and on the gap in federal law that left forced labour without a debt unpunished.",
  "units": [
   (15, "Some coercion of this sorry labor", IC.format("445–446"),
    "Possibly the most widely heralded case of alleged peonage was that connected with the building of the extension of the Florida East Coast Railway. These allegations were investigated by the Bureau of Labor, by the governor of Florida, and by the Immigration Commission. A member of the Commission went to all of the construction camps in existence in 1909, and was permitted free and untrammelled conversation with the men there employed. Members of the Commission also examined the officers of the road, former employees in the hospital at Miami, and even prisoners in the chain gang on the streets in Miami. All of these investigations indicate that from the beginning the officers of the road issued strict orders against either brutality toward the men or acts in the nature of peonage or illegal restraint. In the beginning, however, of the organization of this large force of 4,000 men the company suffered from the carelessness—to use no harsher term—of the labor agents in New York City, who, in receipt of commissions for each man sent, recruited many men totally unfit for construction work, numbers of whom had no intention of ever even going to Florida, and 25 per cent of whom, as a matter of fact, never did reach any of the construction camps. In some of the camps in the earlier days there was some coercion of this sorry labor; there were attempts to compel individuals to work, and some foremen who indulged in these practices were discharged by the company. Neither the governor of Florida, the Commission, nor the Department of Justice has been able to find anything in the nature of legal proof that peonage ever existed upon any of this work of the Florida East Coast Railway. Men were found in 1909 who had left the work as many as three times and were in their fourth employment. These men testified that their treatment had been good throughout. In one or two instances men who came in the early days of the work had remained and risen to positions of some responsibility. The cases in which agents of the company were sought to be convicted of peonage in no instance resulted in a conviction.",
    "The Commission visited in 1909, three years after the complaints and the strike of 1905–1906. It found 'some coercion' and dismissed foremen, and no legal proof of peonage."),
   (16, "No punishment for simple slavery", IC.format(446),
    "Federal attorneys and judges in the southern States have been unable to find any provisions in the statutes of the United States imposing penalties for the imposition of slavery unaccompanied by some special feature. It is apparent that Congress has never passed a general measure providing for the enforcement of the thirteenth amendment. … However, if a person simply places or holds another in slavery, it is impossible for the federal courts to impose penalties under statutes at present in vogue, unless the placing or holding be for the purpose of forcing the settlement of a debt, no matter how great may be the abuses perpetrated upon the person held. In the Clyatt case the Supreme Court decided unmistakably that the peonage statute (R. S., 5526) referred only to cases where the return or arrest or holding has been for the purpose of enforcing the payment of a debt. (See Clyatt v. United States, 197 U. S.)",
    "The law the trial of 1908 turned on: unless a man was held for a debt, forcing him to work was not peonage. The omission (…) is the Commission's quotation of two sections of the Revised Statutes."),
   (17, "Sent south from New York City", IC.format(445),
    "In connection with the southern cases it should be noted that in nearly every instance brought to the attention of the Commission the laborers who were held in peonage had been sent south from New York City, the victims of gross misrepresentations by labor agents there as to conditions under which they were to work, and totally unfitted for the work to which they were going.",
    "Said of the southern cases in general, on the page before the Florida East Coast case."),
  ]},
]


COMPARE = [
 {"id": "held1908", "titel": "Were the men held against their will?",
  "frage": "Locked trains and beatings, a job any man could leave, or 'some coercion'?",
  "note": "The prosecutor in 1908 described locked trains, armed guards, a fire hose and beatings, from the men's letters. Spooner in 1907, travelling with the railway's engineers, quoted a worker who said any man could leave by refusing to work, and traced the stories to the chain gang. The Immigration Commission, visiting in 1909, found 'some coercion' in the early camps, foremen dismissed for it, and no legal proof of peonage. The law in force punished forced labour only when it was tied to a debt.",
  "voices": [{"text": "labour", "sec": "trial", "n": [12]},
             {"text": "labour", "sec": "chain", "n": [9, 10]},
             {"text": "labour", "sec": "commission", "n": [15, 16]}]},
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
        "titel": "Recruited in New York: wages, deductions, the chain gang and the peonage trial",
        "autor": "F. E. Spooner in The Railroad Gazette (1907); L. M. Thacher to the Engineering Association of the South (1911); Frank M. Patterson in the Railway Age Gazette (1912); the Associated Press (1908); the Immigration Commission (1911)",
        "jahr": "1905–1912",
        "quelle": "F. E. Spooner, \"Building the Florida East Coast Extension to Key West,\" The Railroad Gazette 42:17 (26 Apr. 1907), pp. 583–584 (archive.org sim_railway-age_1907-04-26_42_17); L. M. Thacher, \"Key West Extension of the F. E. C. Ry.,\" Engineering Association of the South, vol. XXII (1911), p. 72 (Google scan reproduced in https://historicbridges.org/florida/sevenmilebridge/articles.pdf); Frank M. Patterson, \"The Florida East Coast Extension,\" Railway Age Gazette 52:19 (10 May 1912), p. 1041 (archive.org sim_railway-age_1912-05-10_52_19); Associated Press, New York, 13 Nov. 1908, in The Paducah Evening Sun, 14 Nov. 1908 (Library of Congress, Chronicling America, sn85052114); Reports of the Immigration Commission, Abstracts of Reports, vol. 2 (S. Doc. 747, 61st Cong., 3d sess., 1911), pp. 445–446 (archive.org abstractsreport01benngoog). All public domain: published in the United States before 1931; the Commission's report is a federal publication.",
        "hinweis": "Every passage was read against the page image. The workers speak here only twice: through the prosecutor who repeated what they wrote in their letters, and through one unnamed man questioned by Spooner. Everything else is the railway's engineers, the railway press and a federal commission that came three years later. Their judgements on whole groups of workers are quoted as printed. The trial's outcome is carried in the railway's own account; a contemporary report of the verdict has still to be found.",
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
