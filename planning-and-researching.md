Firstly, I am thinking of smth in flask/python, but for hackclub to make it easier for the reviewers, it should be easily accessed and tested. So probably a flask web app would be nice idea, hmm.
If I make smth like studying, where users are basically A level/CIE  sutdents and they can track there assignments, deadlines and subjects, and upload study resources in one place? Oh it would be really cool to make like smth like a OS system, yk basically where u can drag and drop stuff, and we have an AI in space, basically a Big board where everything can stay
Ya it seems nice I am going with smth like studyhub, AI based/powered board kinda thing, the one that also helps in study and managing, and sorts the stuff automatically. 
Now lets thing of what would we be needing??; for now what comes to mind is, SQlite for database and login stuff, lets do flask for web making, lets just search stuff
Wait before we go on to knowing technacalities, lets first think or what features we need, rn I am thinking of making it for me and students like me, I am doing  A level CIE, and exams comes in like 170days and I have studied nothing, maybe smth that guides me to daily study? I would want smth that kinda forces me, I am still into the OS vibe yk full personal space; and I am leaning into yk more into pastpaper forced, because I have heard they are the best resource, so we could make smth that gives us our exam deadlines, give yk that ahh paper is coming things, and then we'll also be uploading notes that we can easily access and use it to chat with AI, we'll make it so algorith sorts them automatically to the users relevant subjects in A level, and then when studying we can directly opens notes, past papers and even we can do pastpapers on the OS? yk good writer tool? and then we can use AI to check yk the paper with the markscheme of that specific year and mark it. I feel like this thing is so good aahaha.
Ok so far Features Stack
"@FEATURES: 
# 6:40/ 9-11 (you its 9-11 hahaha)
1. full board/OS vibe, pan/zoom/move
2. upload any notes and it auto-sorts using an python algorith
3. AI that helps plan how to study and rely heavily on past papers practice even if u are starting from scratch
4. you can select and do past papers in that system and if you want You can just simply solve there and AI would take relevant Mark scheme and marks ur paper
5. AI can error log ur mistakes from pastpapers in proper section, so u dont have to manually write down ur mistakes.
6. If possible it can automatically makes flashcard for u of ur mistakes."
# 6:50 / 9-11
7. analysis screen that tells whats done and how my progress is going and stuff like that

Ok this seems nice, and i'll add time/date tag when I am adding new features or smth comes mind while building, also lets make it kind like checklist.
Now what? maybe lets now make list of what things ill be using yk the tech stack!

"@Tech Stack:
# 6:49 / 9-11
1. Flask
2. Python
# 6:52 /9-11 some intensive research (trust me dude, it aint AI)
3. SQlite (for database, I had alr said that yk before)
4. Jinja2 template and bootstrap 5
"

I did some more research and it seems like the AI canvas is really hard, but yk what is life without trying?? lets go with it for now, also yk AI is expensive, so my plan is to either use yk hackclub free AI api (hahahah) or I could just use KILO gateway or smth like that, IK it have some free vision model, lets just check if hackclub one has vision. 

Ok so definitely gonna use hackclub one, cuz it have alot of model, we'll decide the model later, for now I was thinking yk we can also implement yk that JEV AI in our app?? maybe for paper checking, cuz normal llm hallucinate and jev, would just look at context(Mark scheme) and then see our answer and then will give percentage of how much right I am, and we can then just convert that percentage into marks thruh some math IK

hmm, so I think lets start working now and firtly lets setup the coral and then start with making environment here

Lets first start by initiating git and make a github repo

also bro we'll change the name of it, as its too generic, like who tf gives there project name like "StudyHub", whatever, IDK if ill devlog more, lets see how it goes. 

Why is the work I am doing on terminal not being counted??

OK I have decided the name, it should be called, StudyAL *IK its not great but better than studyhub*

