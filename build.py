"""Generates index.html for liljanabottigliero.com from the content scraped off the Wix site."""
import html, sys, json

OUT = sys.argv[1]
NP = "https://northpointenow.org/"
e = html.escape

WORKS = [
  # (year, kind, title, link, image, credit, reflection)
  ("fr", "Review", 'Reflecting on "Who I Am"', NP+"reflecting-on-who-i-am/", "who-i-am.png", "Yana Bottigliero",
   "When this story idea was being discussed, I knew that I had to jump on it. It was a review for singer-songwriter Shawn Mendes's self-titled album. Mendes's pop work until then had been a major part of my childhood, and as he was headed into a new genre, my curiosity piqued. As someone who tends to like everything, I worked hard to create an opinionated review with strong musical vocabulary, a solid background on Mendes and recommendations on groups who would like his album. This was also the first piece I wrote myself, and the first time I made and taught myself the basics of digital art. While looking back, I wish I represented more of Mendes's personality in the digital art, I'm still glad to have stepped out of my comfort zone into a skill I will be working to improve in the future."),
  ("fr", "Feature", "Saved by the style", NP+"saved-by-the-style/", "saved-by-the-style.png", None,
   "Being a millennial at heart, when we decided that the feature story for our November issue would be 90's trends resurfacing in Gen Z culture, I was over the moon. Even though we had settled on this evergreen topic after the original idea was scrapped, I am very proud of myself and my story partners for whipping up this interesting story. There are many amazing aspects to this article, such as tying together individual experiences to represent the range of the millennial generation and incorporating that with a comment on Gen Z thrifting culture. However, I do think we missed capturing the true essence of 90's style in our clothing selections for our digital art because that part was very last minute. From this piece, I learned the importance of properly taking time during an interview and not rushing every question. The main thing that I took away from this experience is not to try to guide an interview, but to have it guide you."),
  ("fr", "Playlist", "90's Forever", "https://open.spotify.com/playlist/0yZAup4pHDXFUPHn2FR38d", None, "Yana Bottigliero",
   "This is the playlist that I made for the Saved by the Style story. I chose to do the playlist because, as an avid fan of 90's culture, I was confident in my ability to curate an accurate mix that captured the diverse 90's spirit. I feel that this playlist is extremely authentic and non-stereotypical, which was one of my goals. However, I do feel that I may have leaned into the alternative genre (which I do favor) a little too much as opposed to the pop and hip-hop genres. That being said, I learned not to leak my personal preferences into my non-opinionated work. My goal is also, when writing or designing a story with a main idea but smaller categories, to give an equal share to all of the categories."),
  ("fr", "News", "Checking out the new independent reading policy", NP+"checking-out-the-new-independent-reading-policy/", "independent-reading.png", "Yana Bottigliero, Lainey Beland and Katie Madigan",
   "This was my first ever story for North Pointe! In my school district, a new policy came into place starting in the fall of 2024 where each English class had to have an independent reading session. My mentor wanted to show me and the other intern under her wing the ropes of journalism by guiding us on our first piece. I think the lede paragraph was very descriptive and flowed greatly, as well as the point of the policy being explored quite well. However, I do think that we could have done better with the visual art, and used a better layout to make more of a visual story as well as a written one. Some of my first steps to improving my digital art, however, have been learning to spread out visuals in an article instead of simply condensing them in a big picture. My goal is to use more visual story layouts in the future."),
  ("fr", "Playlist", "Cozy Autumn Study", "https://open.spotify.com/playlist/47leU2sehznzCQlvnT7iHZ", "cozy-autumn.png", "Yana Bottigliero",
   "For our first issue, I knew my classmates and peers needed a way to lock into their schoolwork after the noisy, lazy summer had just ended. That's why I went to our editorial board and pitched making a study playlist to help transition the aloof summer mindset into a focused autumn one. This playlist is a collage of slow-paced, tranquil songs that are completely study-friendly. The strength in this work is the song collection, as it is genre-diverse, yet somehow all portray the spirit of fall. The digital art, set in my own kitchen, does set the scene for a cozy fall study night. I do wish that I had incorporated the candle more into the frame, as it gives the shot an ethereal glow. I have learned from this piece the subtle importance of placing objects systematically in a picture to set a scene, and my goal derived from this is to use this technique in my photography work in the future."),
  ("fr", "Editorial", "Embracing Irish history in St. Patrick's Day celebrations", NP+"embracing-irish-history-in-st-patricks-day-celebrations/", "st-patricks.png", "Yana Bottigliero",
   "As a native Chicagoan, St. Patrick's Day always meant a big, festive party filled with drinking, cloverleafs and corned beef. It was a big change to team up with my mentor, who is ethnically Irish, to write about the traditional side of the holiday, and how it can negatively stereotype the Irish. From this, I learned that there are often many points of view in a story, and as a journalist, I have to cast aside my bias to extract as many of these as I can and present them to the audience so they can make their own opinion on the matter. As this was my second opinion piece, this article contains a strong argument backed by solid statistics and facts. However, I do wish we had cited more sources for this article and provided more data besides the drinking aspect of St. Patrick's Day. This was also the second article in which I did digital art, and I can definitely say it improved a lot. I also learned how to incorporate metaphors and major themes into my art to better emphasize them to my readers."),
  ("fr", "Infographic", "EU leaving the US behind", NP+"eu-leaving-the-us-behind/", "eu-infographic.jpg", "Yana Bottigliero and Lainey Beland",
   "For our news article on the EU moving forward with support of Ukraine and defense policies despite the U.S.'s pullback, I pitched to my story partner an infographic of a map of the EU mixed with events regarding the article and the locations where they took place. What we came up with is what I consider to be one of my best visuals yet. This is a piece that would easily catch any reader's eye with its bright color scheme. It also delivers facts that add onto the article concisely, so even people who don't enjoy reading articles can take something away from it. However, I do wish we had centered the visual more and done a better job of inserting the textboxes. Overall, one subtle yet crucial skill that I have taken away from this experience is the importance of formatting minuscule details, sources and credits in a way that is aesthetically pleasing."),
  ("fr", "Feature", "Grosse Pointe's representation in the media", NP+"grosse-pointes-representation-in-the-media/", "grosse-pointe-media.png", None,
   "Over the years, my town has gained quite a bit of representation in mainstream media. I was elated when my evergreen topic, displaying the portrayal of our town in the media, was chosen for a web story in our April issue. I think that the writing in this article shines bright. In particular, I adore the descriptive language that we used. We also included cited facts and history in this article, so it was an amazing blend of data and imagery. I do wish we had come up with a catchy and creative title. A skill I learned was using a metaphor mentioned in one interview and snowballing it into a major theme of the article, as if the sources were writing this piece themselves."),
  ("fr", "Photostory", "Performing around the clock", NP+"performing-around-the-clock/", ["photostory-1.jpg","photostory-2.jpg","photostory-3.jpg","photostory-4.jpg"], "Yana Bottigliero",
   "This is the first piece that features photography I've done myself! Photography is a skill I wanted to work on, and I'm so glad to say I got the chance to! This was a picture story of Grosse Pointe North's production of All In The Timing, and I definitely learned the sections in a photostory, including background information, scene context and interviews. The strengths in this story are the witty captions and the brief interviews with the actors, and tying those with their performance. As this was my first time with photography, some angles are a bit off and some shots are blurry, but those are skills I hope to fix with experience behind the camera."),
  ("fr", "Feature", "Tracking down public transportation", None, "public-transportation.jpg", "Yana Bottigliero and Katie Madigan",
   "The experience of working on this collection of case studies is what introduced me to the art skill of telling a story through an infographic. This feature showcases transportation in Detroit, New York City and Chicago through the lenses of people who have commuted on them. It is a wonderful mixture of research and facts with the human element. It was also wonderful to learn how to concisely fit the gist of a story into an infographic for visual appeal and for those who would prefer only a quick look at a story. While the writing is very strong, I wish we had focused more on including more information and detail on the infographics."),
  ("so", "Review", "TS12: Chart topper or total flopper?", NP+"ts12-chart-topper-or-total-flopper/", None, None,
   "I am a loud and proud member of the Swiftie cult. When Swift released her twelfth studio album, \"The Life of a Showgirl,\" I was desperate to review it. I partnered with my friend Jay, who had an opposing opinion of the record. Together, we created a well-balanced review with two contrasting viewpoints, and I learned a lot about bringing different perspectives to a story. While one strong part of this review is my writing, I do wish I had reviewed this album more strictly and had less of my bias get in the way, as well as doing some fun visuals."),
  ("so", "News", "Government shutdown", "files/pdf/government-shutdown.pdf", "page-government-shutdown.jpg", None,
   "One goal the executive board made for the 2025-2026 North Pointe run is to get more expert sources out of our school and into our community. I took on the story of the government shutdown to challenge myself, which was hard to do because some government workers are not allowed to talk about their work. However, my effort was indeed successful; I managed to interview a government worker in another section of our town. The solid point of this story is definitely the diverse sources, ranging from people affected to people who can explain what caused the shutdown, and what we can expect. However, we definitely should have incorporated a picture instead of a graph. As I am continuing my North Pointe journey as the News Section Editor, I hope that I can increase the amount of pictures on my page instead of infographics, so we can tell a story with actual people in them, not just stats."),
  ("so", "Feature", "One holiday season, many traditions", NP+"one-holiday-season-many-traditions/", "holiday-traditions.png", "Yana Bottigliero",
   "Ever since I was a little kid, I have always been fascinated by how different cultures celebrate the holidays, even though it is sometimes referred to as only the Christmas season. I joined this story to help display what different holidays our community celebrates besides Christmas. The staple feature of this article is definitely the abundance of visuals, from the timeline of different holidays celebrated to personal pictures and quotes from sources celebrating these holidays. However, I wish we could have found a source who celebrated Hanukkah; no one would bite, so we had to settle for someone who celebrated Christmas differently. From this story, however, I did learn to be more flexible and to pivot a story when needed, a crucial skill in the journalism world."),
  ("so", "Art", "Lights, Camera, Code", "files/pdf/lights-camera-code.pdf", "lights-camera-code.jpg", "Yana Bottigliero",
   "I am very grateful to have a bit of artistic ability, and I was more than happy to design a piece of art for my page to accompany a news story on how AI is influencing the entertainment industry. I decided to display actors' acceptance speeches for the acting awards they received, with harsh red lettering, because many people believed they didn't deserve the award due to the movies they starred in using AI. While I do love the feelings I evoked in this piece, I wish the placement of the lettering were not so sloppy, and that it were portrayed in a neutral light, so as not to convey bias. Even so, from this piece, I did indeed learn how visuals can sway a reader's opinion on a topic, and how to apply that to more editorial stories. That being said, I still have a long way to go in informing people in a non-biased way through visuals and improving their quality."),
  ("so", "Art", "Parking ban news brief", "files/pdf/parking-ban.pdf", "parking-ban.jpg", "Yana Bottigliero",
   "This is (finally) one non-biased infographic for a story I made! At the start of the school year, our high school administration banned parking on a neighborhood road very close to the school. For a more creative and interactive infographic, we decided to survey how many students were for or against the ban. The strengths are the pop-out colors that catch your eye and add to the story's context. However, again, it could be a lot less sloppy, which is still something I must work on in the future, but I did learn and perfect how to add an unbiased element to a story to not sway readers' opinions, but instead to provide context and two different sides on the matter."),
  ("so", "Editorial", "Love, actually", "files/pdf/love-actually.pdf", "page-love-actually.jpg", "Yana Bottigliero",
   "For anyone who isn't in a relationship (especially in high school), Valentine's Day can really be a drag. However, as someone who is both chronically single yet appreciates all forms of love, I wanted to convey to my school that you don't have to be in a romantic relationship just to celebrate love. My personal, tongue-in-cheek and slightly self-deprecating sense of humor is brilliantly highlighted throughout this piece. I do wish, though, I could have made my point clearer and referenced the article's namesake (which just so happens to be one of my favorite rom-coms of all time). One big boost I learned from this, though, was how to be vulnerable in my editorial articles, as in journalism, the ability to convey ethos in sensitive and moving pieces is indeed a crucial skill to have."),
  ("so", "News", "Breaking Boundaries", "files/pdf/breaking-boundaries.pdf", "page-breaking-boundaries.jpg", None,
   "An act being debated in the Michigan legislature was that families, not borders, would determine which school districts their children would attend. This debate has been going on in Grosse Pointe for quite some time due to worries that allowing more students would weaken the education of our school district. I teamed up with the then Co-Editors-in-Chief to write this story. My favorite part of working on this was stretching out of my comfort zone by enforcing our 2025-2026 year goal of using sources outside our school and interviewing a local parent and even a school board member about their opinions. I do wish we had gone into detail in this article about what Grosse Pointe North becoming a school of choice would have looked like, or should have avoided the topic altogether, since it was still being debated in the legislature with a bleak chance it would actually happen. With the gain of authority as one of the two editors-in-chief, I will strive to write stories that are relevant this upcoming year and listen to students to hear what topics they want to read about."),
  ("so", "Photo", "Breaking Boundaries (art)", "files/pdf/breaking-boundaries-art.pdf", "breaking-boundaries-photo.jpg", "Yana Bottigliero",
   "This was the art, produced by me, that accompanied the Breaking Boundaries news article. It is a shot of students walking out of my school at the end of the day. This actually had me standing on an island in the middle of the road to take this picture, and I had to wait for the rush of cars to pass by for fifteen minutes. However, this shot was definitely worth it, as it represents the student culture of North, and can be used for another story if we are short on art. I wish the picture were more level, even though I was able to get rid of the uneven angle in InDesign, the app we use for page designs. As the new Digital Editor-in-Chief, I will need to rely on visual elements to draw our readers in, and this gave me more practice to use next year."),
  ("so", "Editorial", "The biopic: Informal or invasively inaccurate?", None, None, None,
   "I have always been so upset when women in pop culture, such as Diana Spencer and Marilyn Monroe, who contributed so much to charity and advocated for change, are just reduced to a sex symbol or a victim of circumstance. You can imagine my disgust when \"Love Story\" depicted CBK, an ambitious and private woman, as merely a problematic, messy character. I teamed up with my friend Maddie to explore how CBK and Lady Di's stories are exposed in the media, with their trauma being exploited in such an offensive way. The argument and writing are absolutely amazing, as well as the student-drawn art. However, I wish we had stretched this beyond two case studies to a general trend on how women's stories are treated in the media. This is important as to understand our world as a journalist, you must observe patterns and trends. This has taught me to bring a popular trend and connect it to a bigger issue, which will surely help me as I have to appeal to a digital audience that is focused on trends in my role as Digital Editor-in-Chief."),
  ("so", "Editorial", "Gen Z's spring break", "files/pdf/gen-z-spring-break.pdf", "page-gen-z-spring-break.jpg", None,
   "I am a BIG millennial at heart, and I am also a huge fan of travel. Both of these parts of me bled into this editorial I co-wrote, which is a study on how spring break vacations transformed from a lively and free phenomenon in the 90s to what they are today, planned around curating the perfect post for social media. My persuasive voice really stands out in this, as I compare the energetic feel of letting loose on MTV Spring Break to the constraints a teenager faces today, making sure everything they do on spring vacation is literally picture-perfect. One thing I would have liked to change is the visual, which was last-minute, to convey a comparison between then and now, not just a generic sunset picture I borrowed from my father's recent trip to California. What I learned from this piece is to use a mix of ethos and pathos in editorial writing to convey my argument."),
]

AWARDS = [
  ("2026", "2nd Place", "News Analysis"),
  ("2026", "Honorable Mention", "Editorial / Opinion Page or Spread"),
  ("2026", "Honorable Mention", "News Page or Spread"),
  ("2025", "Honorable Mention", "In-Depth Feature"),
  ("2025", "Honorable Mention", "Review"),
  ("2025", "Honorable Mention", "News Story"),
]

def card(w, i):
    year, kind, title, link, img, credit, text = w
    kslug = kind.lower()
    if isinstance(img, list):
        media = '<div class="media grid4">' + "".join(
            f'<img src="files/img/{s}" alt="{e(title)} photo {n+1}" loading="lazy">' for n, s in enumerate(img)) + "</div>"
    elif img:
        media = f'<div class="media"><img src="files/img/{img}" alt="{e(title)}" loading="lazy"></div>'
    else:
        media = f'<div class="media type"><span>{e(kind)}</span></div>'
    if link:
        ext = ' target="_blank" rel="noopener"'
        label = "Read the page (PDF)" if link.endswith(".pdf") else ("Listen on Spotify" if "spotify" in link else "Read on North Pointe")
        cta = f'<a class="cta" href="{e(link)}"{ext}>{label} <span aria-hidden="true">&rarr;</span></a>'
    else:
        cta = '<span class="cta muted">Print edition</span>'
    cred = f'<p class="credit">Credit: {e(credit)}</p>' if credit else ""
    return f'''<article class="work" data-kind="{kslug}">
  {media}
  <div class="body">
    <p class="kicker">{e(kind)}</p>
    <h4>{e(title)}</h4>
    {cred}
    <details><summary>Her reflection</summary><p>{e(text)}</p></details>
    {cta}
  </div>
</article>'''

fr = "\n".join(card(w, i) for i, w in enumerate(WORKS) if w[0] == "fr")
so = "\n".join(card(w, i) for i, w in enumerate(WORKS) if w[0] == "so")
kinds = sorted({w[1] for w in WORKS})
filters = '<button class="chip on" data-f="all">All</button>' + "".join(
    f'<button class="chip" data-f="{k.lower()}">{k}</button>' for k in kinds)
awards = "\n".join(f'<li><span class="yr">{y}</span><span class="place">{p}</span><span class="cat">{c}</span></li>' for y, p, c in AWARDS)

person = {
  "@context": "https://schema.org", "@type": "Person",
  "name": "Yana Bottigliero", "alternateName": "Liljana Bottigliero",
  "url": "https://liljanabottigliero.com/",
  "image": "https://liljanabottigliero.com/files/img/hero.jpg",
  "jobTitle": "Digital Editor-in-Chief, North Pointe",
  "affiliation": {"@type": "HighSchool", "name": "Grosse Pointe North High School"},
  "email": "mailto:liljana.bottigliero2028@gmail.com",
  "award": [f"{y} MIPA {c}, {p}" for y, p, c in AWARDS],
  "knowsAbout": ["Journalism", "Digital media", "Infographics", "Photography", "Editorial writing"],
}

page = open(sys.argv[2]).read()
page = (page.replace("{{FRESHMAN}}", fr).replace("{{SOPHOMORE}}", so)
            .replace("{{FILTERS}}", filters).replace("{{AWARDS}}", awards)
            .replace("{{COUNT}}", str(len(WORKS)))
            .replace("{{JSONLD}}", json.dumps(person, indent=2)))
open(OUT, "w").write(page)
print("wrote", OUT, len(page))
