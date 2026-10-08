"""Build data/act.json, module 7: 2 September 1935, the veterans, the train, and 'an act of God'; the end of the line.

Sources (public domain, federal publications), each passage read against the page image unless noted:
- W. F. McDonald, "The Hurricane of August 31 to September 6, 1935," Monthly Weather Review 63:9 (September 1935),
  pp. 269–270 (archive.org sim_monthly-weather-review_1935-09_63_9, n0–n1).
- U.S. House of Representatives, Committee on World War Veterans' Legislation, Florida Hurricane Disaster: Hearings
  on H.R. 9486, 74th Cong., 2d sess. (Washington: GPO, 1936) (Google Books id sgsXAAAAIAAJ, page images):
  p. 332 (statement of Conrad Van Hyning), pp. 437–441 (report of Aubrey W. Williams and George E. Ijams to the
  President, 8 September 1935), pp. 441–442 (testimony), pp. 504–506 (statements and letters of the Florida East
  Coast Railway).
- Florida East Coast Ry. Co. Abandonment, 217 I.C.C. 325 (1936), pp. 328–330 (Google Books id lAYXAQAAMAAJ).
- C. R. Vinten, "A Highway Over the Sea," The Regional Review (National Park Service) 1:1 (July 1938), read in the
  transcription at https://npshistory.com/newsletters/regional_review/vol1-1c.htm (no page image reached).
Run from the repository root:  python tools/build-act.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "act.json"

MWR = "Mon. Weather Rev. 63 (1935), p. {}"
H = "Hearings on H.R. 9486 (1936), p. {}"
ICC = "217 I.C.C. 325 (1936), p. {}"
NPS = "Regional Review 1 (1938)"

SECTIONS = [
 {"id": "storm", "zk": "Storm", "titel": "The storm, 2 September 1935",
  "blurb": "The Weather Bureau's account of the hurricane on the Upper Keys, and the log of its observer at the fishing camp on Long Key, over which the centre passed.",
  "units": [
   (1, "Practically complete", MWR.format(269),
    "Over a distance of about 30 miles, from the settlement of Tavernier (about 25°01′ N., 80°32′ W.) to Vaca Keys, the destruction of buildings, roads, viaducts, and bridges was practically complete. Much of this damage was caused by the overwhelming depth and strong washing flow of the storm tide that piled up on the Keys under the driving power of the storm. The tracks of the Florida East Coast Railroad were completely destroyed where they crossed between islands and were shifted bodily off their roadbed over long stretches on the Keys. An 11-car train, sent to Lower Matecumbe Key in an effort to rescue inhabitants, was washed from the tracks and only the locomotive withstood the force of wind and tide.",
    "'Viaducts, and bridges' were destroyed, the Weather Bureau says; the railway's application of 1936 speaks of roadbed and track (module 6 [7]), and in 1938 the new road bridges stood on the old piers ([23])."),
   (2, "Thirty feet above the water", MWR.format(269),
    "The disposition of debris and nature of the erosion of the railroad embankments clearly indicate that the destructive tide flowed with intense effect over the Keys from southeast to northwest, in the direction of advance of the storm center. As is usually the case, the destructive effects extended considerably farther to the right than to the left of the path of the center. Had there been no accompanying tide, the damage undoubtedly would have been severe but by no means so complete as that resulting from the tidal inundation. The track and crossties of the railroad were in one stretch washed off a concrete viaduct 30 feet above ordinary water level, but wave action superimposed on the tide no doubt play tides [sic] part in this destruction.",
    "The printing has 'play tides part', evidently for 'played its part'. The track went off the viaduct; the viaduct stayed."),
   (3, "Water 3 feet from top of railroad grade", MWR.format(270),
    "6:45 p. m.—Barometer 27.90. Wind backing to NW., increasing; plenty of flying timbers and heavy timber, too—seemed it made no difference as to weight and size. A beam 6 by 8 inches, about 18 feet long, was blown from north side of camp, about 300 yards, through observer's house, wrecking it and nearly striking 3 persons. Water 3 feet from top of railroad grade, or about 16 feet. 7 p. m.—We were now located in main lodge building of camp; flying timbers had begun to wreck this lodge, and it was shaking on every blast. Water had now reached level of railway on north side of camp. (Ed. Note.—This was water rapidly piled up from the shallow expanse of Florida Bay, under the drive of northerly hurricane winds.)",
    "J. E. Duane, the Weather Bureau's cooperative observer at the Long Key fishing camp. The water from Florida Bay piled up against the line, as the engineers had found in 1909 and 1910 (module 5 [11])."),
   (4, "Three populous relief work camps", MWR.format(270),
    "The loss of life on the Keys was very heavy. Three populous relief work camps inhabited by war veterans were destroyed. The best estimate of mortalities, furnished by the American Red Cross, places the total at 409, of which number 244 are known dead and 165 missing.",
    None),
  ]},
 {"id": "camps", "zk": "Camps", "titel": "Why were the veterans on the keys?",
  "blurb": "The veterans were unemployed men of the First World War in the relief work camps of the Federal Emergency Relief Administration on the keys; the committee's chairman called them 'these same men' whom a former administration had driven out of Washington 'at the point of a bayonet'. In the hearings of 1936 Representative Rogers asked why they had been sent there.",
  "units": [
   (5, "Knowing that they have hurricanes there", H.format(441),
    "Mrs. Rogers. How did you happen to select Matecumbe Island, knowing that they have hurricanes there, rather than some other place in the United States, where they have no hurricanes? The Chairman. Of course, Mr. Williams, you are not an expert on hurricanes, are you? Mr. Williams. No. The Chairman. I was going to suggest, if you were, I would like very much to have your services from now on. Mr. Williams. As was brought out by Mr. Stone, Mrs. Rogers, this matter was handled by our agent, or the agent of the Governor in Florida.",
    "Aubrey W. Williams, assistant administrator of the Federal Emergency Relief Administration, questioned by the committee."),
   (6, "Cheaper where it is warm", H.format(442),
    "Mr. Williams. We selected Florida and other Southern States down there for, I would say, two or three reasons. The first reason was the cost of maintaining men in a camp is smaller in a section of the country that is warm, where you do not have the expense of heating, and the necessity of more adequate and complete buildings, and so forth. That was one factor. Another factor was we had in Mr. Stone an imaginative and resourceful person who could and was, in our estimation able to, make profitable use in the way of work, to develop profitable work whereby these people could earn their wages. The third reason was that we did not receive any general cooperation on the part of a great many States upon our request that these men be organized and put into work projects.",
    "Cost first. Thirty years after the quarterboats of 1906, men were again housed cheaply on the keys in the hurricane season."),
   (7, "Strain or stress", H.format(442),
    "Mrs. Rogers. You felt that it was important to send them to a place where they would be under no stress or strain, under the circumstances? Mr. Williams. I was never conscious that we had any places where the men were under restraint. Mrs. Rogers. No; I said strain or stress. I am speaking of such things as storms. Of course, they do have storms in Florida. For instance, if you go to a travel agency, if you intend to take a trip, during those hurricane months they advise you to take your trip in some other month. So we know that that situation exists.",
    None),
  ]},
 {"id": "train", "zk": "Train", "titel": "The train",
  "blurb": "In May 1935 the director of the veterans' camps asked the railway for trains to take the men off the keys in a hurricane. The railway's answer, its conditions, and its account of the train that left Miami on Labor Day afternoon, printed in the hearings of 1936.",
  "units": [
   (8, "From 12 to 24 hours", H.format(505),
    "We have approximately 700 veterans and civilians employed in my Department whom it will be necessary to move. We will need two trains made up as follows: One baggage car for field kitchen equipment; one baggage car for food supplies, and one baggage car for personal belongings, in addition to a sufficient number of day coaches to handle approximately 350 men. As I understand it, your day coaches have a capacity of 80 persons and in that case, it will necessitate five coaches. It is desired that this equipment be kept close enough to the key area in order that we may secure this service from your railway on short notice; say, from 12 to 24 hours before a hurricane would strike the keys. Since your passenger schedule between Jacksonville and the key area is only about 10 hours, I do not believe it would be necessary to keep the equipment in the Miami area. The object in this is to eliminate any cost to our organization on account of your storing your equipment at Miami specially for this service.",
    "F. B. Ghent, director of the veterans' work program, to S. M. Loftin, co-receiver of the railway, 16 May 1935. Again the cost: the equipment was not to be kept at Miami."),
   (9, "Twelve hours' notice", H.format(505),
    "In every case of disturbance of any intensity, we receive through the Weather Bureau sufficient advance notice to enable us to furnish locomotives and equipment to make up two trains, and they would be available after receiving 12 hours' notice of your desire for them. In the event it is deemed advisable to move the veterans upon receipt of report of an approaching storm, the railway must be advised definitely to what point the veterans will be moved to get them to safety. In other words, we will have to know definitely between what points the relief trains will be operated in order that we may make necessary arrangements for taking care of the equipment, and the train crews after the trains arrive at destination, also that the railway will not be subject to protest from any community to which the veterans will be transferred, with regard to sanitary and other conditions.",
    "The railway's co-receiver to Ghent, 6 June 1935."),
   (10, "Not to move a special train", H.format(506),
    "Having received instructions from the receiver's office on September 1 not to move a special train of this kind to any point unless we had assurance that the F. E. R. A. officials had first made arrangements with the municipal officials of the city to which the men were to be taken, I inquired of Mr. Ghent whether he had arranged with the Hollywood authorities for the men to be encamped at that point, advising him that we could not provide sanitary service for the men to remain in the cars, and he replied that all arrangements had been made for the men to detrain at Hollywood on arrival, but he desired the equipment held at that point, so that the men could be returned to the camps as soon as the storm was over.",
    "F. L. Aitcheson, assistant to the railway's general superintendent, statement of 4 September 1935. The call came at 2 p.m. on Labor Day and ended at 2:07."),
   (11, "No switch engine in service", H.format(504),
    "Owing to the curtailed summer service, there was no switch engine in service until 3 p. m., at which time they immediately began collecting the necessary coaches and baggage cars from the yards to make up the train. It was also necessary to pick up three box cars from the yards to attach to the train for the baggage of the men. Instructions were given immediately to have engine prepared and steamed up for the train, and this, under best conditions, takes 2 hours. Notwithstanding the difficulties under which the officials labored, the train was made ready, consisting of engine and 11 cars, and left Miami at 4:25 p. m. It was delayed 10 minutes at the Miami River drawbridge by a stream of holiday motor boats passing through the draw. As there are no means of turning an engine south of Homestead the engine was turned at that point, and the train was backed from there toward the veterans' camps.",
    "Statement issued by Scott M. Loftin, co-receiver of the railway, St. Augustine, 6 September 1935."),
   (12, "Only the engine standing on the track", H.format(504),
    "South of Homestead the train ran into gales, which continued to grow heavier, and the train reached quarry, on Quarry Key, 72 miles south of Miami, at 6:50 p. m. There the train was delayed 1 hour and 20 minutes by obstruction resulting from the storm. When this was cleared up the train proceeded to Islamorada, where it arrived about 8:20 p. m., where it was found that the wires were down, the agent had evacuated the station, the storm had become of hurricane force, and the water had risen to about the level of the floors of coaches. Finally a tidal wave came and turned over all the coaches, baggage cars and the three freight cars, leaving only the engine standing on the track. The train was never able to reach the veterans' camp on Lower Matecumbe.",
    None),
   (13, "Unless the train had left Miami about 10 a. m.", H.format(504),
    "The officials of the railway have cooperated with the F. E. R. A. officials in every way possible since the veterans have been in camps on the keys, and in this instance exerted themselves to the utmost to get this special train out from Miami at the earliest possible time, notwithstanding the many handicaps that existed. From what we know now it seems that the men could not have been evacuated from the camps unless the train had left Miami about 10 a. m.",
    "Four hours before the request for the train was made ([15])."),
  ]},
 {"id": "report", "zk": "Report", "titel": "\"An act of God\": the report to the President, 8 September 1935",
  "blurb": "Six days after the storm Aubrey W. Williams of the Federal Emergency Relief Administration and Col. George E. Ijams of the Veterans Administration reported to President Roosevelt. Their report was printed in the hearings of 1936. The companion game takes its title from its conclusion.",
  "units": [
   (14, "The advisory of 1:30 p. m.", H.format(437),
    "The advisory of 1:30 p. m. Monday, September 2 (issued at 1:45 p. m.) gave the approximate position of the center of the hurricane as latitude 23° 20′, and longitude 80° 15′. This located the center of the hurricane approximately 200 miles east of Havana and 180 miles southeast of the keys. The same advisory stated that the hurricane was moving slowly westward and would be accompanied by winds of gale force on the keys that afternoon and night. The advisory further stated that winds of hurricane force were anticipated in the Florida Straits (south of the keys) on Monday afternoon and night, indicating that the hurricane would pass through the Straits and not across the Keys. The first advisory indicating that the center of the hurricane had turned in a northwesterly direction and was moving toward the keys was issued at 4:41 p. m. on September 2.",
    None),
   (15, "A minimum of 12 hours", H.format(438),
    "Shortly after 1:30 p. m. Mr. Ghent in Jacksonville, who was in telephonic communication with Mr. Sheldon at Matecumbe, being nervous about the situation, made inquiries of his own regarding barometric readings and found that such readings at Matecumbe were below those at Miami and Key West. Based upon this fact, and the advisory of 1:30 p. m., Ghent determined to evacuate the camp. Accordingly at a few minutes before 2 o'clock, he requested the officials of the Florida East Coast Railroad Co., at St. Augustine (the main office of the line) to dispatch a train to the keys at once. Mr. Sheldon states that, when he called the railroad company at Miami on Sunday he was advised that a train would reach Matecumbe (approximately 90 miles south of Miami) 3 hours after the request for a train was made. At the time Mr. Ghent ordered the train he believed that he would have a minimum of 12 hours to evacuate the camps, assuming that the hurricane struck the keys.",
    "Twelve hours was also the notice the railway had asked for in June ([9]). Ghent read the barometer; the advisories said the storm would pass south of the keys."),
   (16, "A holiday", H.format(438),
    "There is some discrepancy in the statements of the witnesses as to the exact time at which the Miami terminal of the railroad received orders to prepare and dispatch the train. It is clear, however, that the order was not received before 2 p. m. or after 2:35 p. m. However, preparations to assemble the train were commenced shortly after 2 p. m. upon receipt of advice at Miami from Sheldon that orders for the dispatch of the train had been placed at St. Augustine headquarters. The fact that a crew had to be assembled on a holiday (Labor Day) together with the time required to collect coaches and to repair one coach, delayed the departure of the train from Miami until 4:25 p. m., approximately 2 hours after orders for the dispatch had reached Miami.",
    None),
   (17, "Does not lie with any of the human factors", H.format("440–441"),
    "In conclusion, after making as thorough and careful an inquiry within the available time at our disposal, which future inquiry now being vigorously pushed will add to, we are of the opinion that responsibility for this disaster does not lie with any of the human factors concerned. Upon the basis of the weather advisories which were issued and all other weather information available, we have no right to assume or hold to the belief that action looking toward the evacuation of the camps was required by those in charge prior to 1:30 p. m. on Monday, September 2. Based upon previous information given by the railroad on Sunday, those in charge had a right to assume that the train ordered at 2 p. m. would arrive in ample time to evacuate the camps. The delays experienced in the arrival of the train at Islamorada after its dispatch had been ordered were probably unavoidable in view of the fact that it was a holiday and unavoidable incidents occurred on the way to the keys. After weighing all of the evidence obtained in as orderly and careful an investigation as it has been possible to make up to this point, it is impossible for us to reach the conclusion that there has been negligence or mistaken judgment on the part of those charged with responsibility for the safety of the men engaged on the keys projects. To our mind the catastrophe must be characterized \"as an act of God\" and was by its very nature beyond the power of man or instruments at his disposal to foresee sufficiently far enough in advance to permit the taking of adequate precautions capable of preventing the death and desolation which occurred.",
    "The report did not ask why the men were on the keys in the hurricane season ([5]–[7]), nor why the trains were not kept nearer ([8]). Its authors were the officials of the two agencies responsible for the camps."),
  ]},
 {"id": "dead", "zk": "Dead", "titel": "Counting the dead",
  "blurb": "As in 1906, each count is different: the interim count of the veterans in the report of 8 September, the Red Cross estimate in the Weather Bureau's report, and the bodies recovered up to March 1936. Photographs of the dead are not shown here.",
  "units": [
   (18, "Identified dead 44", H.format(440),
    "The work of identifying the dead and injured veterans has not yet been completed. The most recent information indicates the following figures: Identified dead, 44. Missing and unidentified dead, 238. Identified injured, 106. Identified uninjured, 296. Total, 684.",
    "The report of 8 September 1935; the table is given here as a sentence. It counts the veterans only."),
   (19, "257 veterans, 228 civilians", H.format(332),
    "Upon the recommendation of the health officers Governor Sholtz issued an order on Saturday, September 6, directing the cremation of all bodies at points near to where they were recovered. … The report lists the known dead as 423 up to November 19, 1935. From November 19, to March 1, 1936, 62 additional bodies have been recovered, making the total number of recovered bodies 485. This figure accounts for all of the bodies identified as veteran dead and missing and for all of the civilian identified dead and missing. It is possible that a few additional bodies will still be recovered as no accurate figure could be secured as to the civilians missing. The following is a summary of the disposition of bodies up to March 1, 1936: Bodies shipped to relatives, veterans 9, civilians 5, total 14. Cremated on Keys, veterans 168, civilians 130, total 298. Woodlawn Cemetery, Federal Emergency Relief Administration, veterans 80, civilians 29, total 109. Buried in private plots and cemeteries on the mainland and the keys, civilians 64. Total, veterans 257, civilians 228, total 485.",
    "Statement of Conrad Van Hyning, administrator of the Florida Emergency Relief Administration, inserted in the hearings. The omission (…) covers the burials at Woodlawn Cemetery and the work of identification. The six lines of civilian burials (Woodlawn private plots 15, Homestead 10, Key West 3, Dania 3, cemeteries on the keys 11, buried where found 22) are summed here as 64. 6 September 1935 was a Friday; the printing says Saturday."),
  ]},
 {"id": "end", "zk": "End", "titel": "The end of the line, 1936–1938",
  "blurb": "The railway did not rebuild. The Interstate Commerce Commission's findings of September 1936, and the highway that the National Park Service described in 1938.",
  "units": [
   (20, "Not practicable at the elevation permitted", ICC.format(328),
    "Immediately after the storm of September 2, 1935, the applicants were notified by the district engineer of the War Department that no reconstruction should be started until plans therefor had been submitted to, and permit issued by, the War Department. The State Road Department took steps to secure the authorization of the War Department to repair the highway, and in that proceeding, after hearing, the War Department limited the height of embankments across waters to a maximum of 5 feet above mean low water, which elevation was lower than that previous to the storm. Property owners appeared at the hearing mentioned to protest the restoration of the previous higher embankments. Because the applicants had definite knowledge of the requirements of the War Department they did not file a formal application for a permit to restore the extension. The minimum cost of reconstruction of the extension within the limitation set by the War Department is $1,800,000. It was testified that it would not be practicable to operate the extension at the elevation which would be permitted. The receivers have not been able to secure funds for reconstruction purposes.",
    "The embankments that had dammed the bay in 1909, 1910 and 1935 were not to be rebuilt at their old height."),
   (21, "$640,000", ICC.format(328),
    "The court having jurisdiction of the railroad receivership proceedings authorized and directed the receivers to file the application here under consideration and, if a certificate permitting abandonment be issued by us, to sell that portion of the right-of-way between Lower Matecumbe Key and No Name Key to the Overseas Road and Toll Bridge District, a political subdivision of the State of Florida, for $640,000, and to sell the remainder to Monroe County, the State Road Department of Florida, and the city of Key West. … The Toll Bridge District will construct a 20-foot highway with funds obtained from the Federal Emergency Administration of Public Works, thereby eliminating the present ferry service, which will reduce the time required for travel by automobile from Miami to Key West from 10.5 to 4.5 hours.",
    "The omission (…) concerns the taxes on the property."),
   (22, "Operated at a loss for some time", ICC.format("329–330"),
    "The testimony is that immediately following the storm it was the view of the inhabitants of the territory served that the extension should be rebuilt, but after they were assured that funds could be obtained for the establishment of the highway and the elimination of the existing ferry service, this attitude changed and now they practically are unanimously in favor of the construction of the highway in preference to the rebuilding of the extension. … The record shows that the extension has been operated at a loss for some time and that there is no reasonable basis for assuming that future traffic and earnings therefrom warrant the reconstruction and operation thereof. Under the circumstances, rehabilitation and operation of the extension would impose an unnecessary and undue burden upon the applicants and upon interstate commerce.",
    "Decided 26 September 1936. The omission (…) covers the request for speed, so that work could be given to residents of Key West on relief projects, and the single protestant's case."),
   (23, "On the piers of the old railroad bridges", NPS,
    "The right of way and bridges of this railroad were purchased by the State for $640,000, which was part of a $3,500,000 loan made to the State by the Public Works Administration. The balance of these funds was set aside for construction of nearly 14 miles of bridges and 30 miles of road over narrow keys, which have closed a gap formerly traversed only by the railroad and ferry. Modern concrete bridges, which have been constructed on the piers of the old railroad bridges, are now open to vehicular traffic and provide a continuous drive from Miami to Key West.",
    "Read in a transcription; the page image of the newsletter was not reached. The piers the company had promised would 'stand firm, unshaken, indestructible' (module 1 [28]) carried the road."),
  ]},
]

COMPARE = [
 {"id": "blame1935", "titel": "Could the men have been saved?",
  "frage": "'An act of God', a train that would have had to leave at 10 a.m., or a question nobody answered?",
  "note": "The report to the President found that responsibility lay with none of the human factors and called the disaster an act of God. The railway's co-receiver wrote that the men could have been saved only if the train had left Miami about 10 a.m., four hours before it was requested. In the hearings Representative Rogers asked why men had been sent to a place known for hurricanes; the answer began with the cost of heating.",
  "voices": [{"text": "act", "sec": "report", "n": [17]},
             {"text": "act", "sec": "train", "n": [13]},
             {"text": "act", "sec": "camps", "n": [5, 6]}]},
 {"id": "dead1935", "titel": "How many died on 2 September 1935?",
  "frage": "684 veterans counted, 409 dead and missing, or 485 bodies recovered?",
  "note": "Six days after the storm the report to the President counted the veterans: 44 identified dead and 238 missing or unidentified among 684. The Weather Bureau printed the Red Cross estimate of 409 dead and missing. By March 1936 the Florida relief administration had recovered 485 bodies, 257 of them veterans; for the civilians, it said, no accurate figure of the missing could be had.",
  "voices": [{"text": "act", "sec": "dead", "n": [18]},
             {"text": "act", "sec": "storm", "n": [4]},
             {"text": "act", "sec": "dead", "n": [19]}]},
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
        "titel": "2 September 1935: the veterans, the train, and \"an act of God\"",
        "autor": "The Weather Bureau (Monthly Weather Review, 1935); the House hearings Florida Hurricane Disaster (1936), with the report to the President of 8 September 1935 and the railway's statements; the Interstate Commerce Commission (1936); the National Park Service (1938)",
        "jahr": "1935–1938",
        "quelle": "W. F. McDonald, \"The Hurricane of August 31 to September 6, 1935,\" Monthly Weather Review 63:9 (Sept. 1935), pp. 269–270 (archive.org sim_monthly-weather-review_1935-09_63_9); U.S. House, Committee on World War Veterans' Legislation, Florida Hurricane Disaster: Hearings on H.R. 9486, 74th Cong., 2d sess. (GPO, 1936), pp. 332, 437–442, 504–506 (Google Books id sgsXAAAAIAAJ); Florida East Coast Ry. Co. Abandonment, 217 I.C.C. 325 (1936), pp. 328–330 (Google Books id lAYXAQAAMAAJ); C. R. Vinten, \"A Highway Over the Sea,\" The Regional Review 1:1 (July 1938) (transcription at npshistory.com). All federal publications, in the public domain.",
        "hinweis": "Every passage was read against the page image except the National Park Service article of 1938, read in a transcription. The hearings were read in the page images of the Google scan; Google's text layer was used only as a draft and corrected at the image. Omissions are marked (…) and explained in the notes. Photographs of the dead survive in federal files; this apparatus does not show them.",
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
