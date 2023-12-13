import json
import subprocess

story_titles = [
    "The Good Fox",
    "Conversations among cats",
    "Tractor gets help",
    "Goldilocks",
    "The memory tree",
    "Cool cat",
    "Scary no more",
    "Naughty Elephant",
    "Save the planet",
    "Professor Blue",
    "Mommy can play again",
    "the fox who wanted to fly",
    "There's a monster",
    "I want to be..",
    "I feel..",
    "Bear Colors",
    "Samis Beach rescue"
]
story_content = [
    """Fox awoke and she was very hungry. She wanted some food for her
dinner.
She walked through the forest to go to the town. Many stores in the
town had food. She needed to find a store with food. She met her
friend, Crow.  He was very hungry , also.
She walked by the toy store. She saw balls  and boats. She saw planes
and trains.  But, she saw no food. The fox was still  hungry and  now she
was sad.
She walked by the clothing store. She saw shoes and shorts. She saw
skirts and shirts. But, she saw no food. The fox was still hungry and now
she was sadder.
She walked by the book store. She saw books about bats and  birds.
She saw  books about monkeys and donkeys. But, she did not see any
food. The fox was still  hungry and now she was even sadder.
The fox walked by the meat market . She saw the butcher chopping
meat into thick slices. The fox wished she could have some meat. Meat
costs money and the fox had no money. She was still very hungry and
very sad.
She walked by the bread and cheese store. She saw a woman making
cheese. The baker was making delicious bread.  The fox wished she
could have some bread and cheese. But, bread and cheese cost money
and the fox had no money. What could she do?
She saw a farmer planting apple trees.  He looked very tired. She
thought, “I should go help him. That would be the kind thing to do.”
The fox ran to the field. She dug holes for the apple trees. She dug the
holes very fast and in a very straight line. The farmer was very happy.
He said “Thank you so much. You look hungry. Go buy some food.” and he
gave her three coins.
She said, “You're welcome.”  She put the coins in her mouth and ran
back to town.
At the bread and cheese store, she  bought bread and cheese. She paid
the baker two coins.
At the meat market, she bought a thick slice of meat.  She paid the
butcher one coin.
She ran by the bookstore. The books about donkeys, monkeys, birds, and
bats were still there.
She ran by the clothing store. The shirt, skirt, shorts, and shoes were
still there.
She ran by the toy store. The train, plane, boat, and ball were still
there.
She ran into the forest. She was still very hungry but now she was
happy.
The fox ran to her den and  saw her friend, Crow. He was sad and still
very hungry.
She gave her friend  the bread.  She barked to call her kits.
  They came out and ate the cheese. She ate the meat.  Crow ate the
bread. Now, everyone is happy and not hungry, anymore. She is a very
good fox.""",
"""“What will we do today?”
“Kill a mouse. What else?”
“Kill a mouse? Do we have to?”
“Yes.”
“Meeow! Well, if you insist.”
“I insist.”
“Come on. Shake a leg! Let's tell
  the others. ”
“Hey, everybody!”
“What's up?”
“Time to kill a mouse!”
“Kill a mouse? Why? Do we have to?”
“Yes. Definitely.”
“But –”
“But me no butts! Mouse-killing time!”
“Are those mouses?”
“What is wrong with you? Those are
leaves! And they're dead already! We
need to kill a mouse. A live mouse! And
by the way, it's mice not mouses.”
“Meeow! A live mouse? You're kidding
me! Kill a live mouse? I don't know about
that. No, that doesn't sound like a very
good idea to me!”
“It's getting late. Seen any mouses? I
  mean mice!”
“Nope! Not a living mouse.”
 “Let's go home so.”
“That's the best idea you've had all
  day!”
“Nothing like a good book and a nice long
sleep! Good night! Sleep tight!”
“Good night! And sweet dreams to all the
mice as well.”
“Oh, the mouses? Yeah, nighty-night
little mouses!” """,
"""This is Lorry .
This is Scooter
Lorry and Scooter are friends.
They are rushing to see theirsick friend, Tractor.
Scooter is going very fast.
Oh no!
Be careful!
Hello friends. I am sick!
Let�s get medicine.
You will be well again!
Tractor is well again!
All of tractor�s friends came to celebrate.
What a party!
Thank you!
Tractor is well again.""",
"""Who goes there?
It’s Mommy Bear, Daddy Bear and Baby Bear.
They often went out for a breath of fresh air!
They lived in a wood
Where the air was quite good!
It smelled of trees
And honey and bees.
They lived a life of luxury and ease.
They loved porridge, it made them strong!
They started each day with porridge and a song:
“Porridge, porridge, full of oats,
 Good for horses, good for goats.
       Please spare a spoonful for poor Johnny Forty Coats!”
This was where they slept at night –
Hoping the nasty bugs wouldn’t bite!
Their dreams were peaceful, often boring.
They didn’t like screaming and shouting and roaring.
One morning, said Daddy, “This porridge is too hot!
Why don ’t we all go out for a trot?”
They liked fresh air – a lot!
They had a little trot and they had a little stroll.
Meanwhile, the porridge was cooling in the bowl!
Who came along but little Goldilocks!
She knocked and she knocked. 
She knocked and she knocked.
“Hey! Hello? I’m not going to knock anymore!
Come on now! Open this donkey-dunderhead door!
My knuckles are getting sore!”
In she did go,
On her tippy-tippy toes.
She tasted the porridge – only Baby’s one was nice!
“The other two porridges? Huh! I’ll leave that goo to the mice!”
She was tired from walking all day in the wood.
And sat herself down, as a little girl should.
Crash! Bang! Wallop! She’d broken Baby’s chair.
“Huh!” said Goldilocks. “See if I care!”
“I could sleep now,” she said with a yawn.
“I could sleep until dawn. ”
That’s what she said
As she lay down gently in Baby’ s bed.
“I’ll rest my head . . .
Yikes! It smells like stale mouldy bread!”
“Hmm . . . something’s queer!
Someone’s been here!”
“Dad! Dad!” shouted Baby Bear.
“Look at my bowl! There’s nothing there!
Who would eat my porridge? Who would even dare?”
“Look over there!” 
screamed Mommy Bear.
“Poor Baby’s chair!
Well, I declare!”
Said Daddy Bear to his precious wife,
“Never seen anything like it in my life!”
Slowly Goldilocks opened her eyes:
Three bears were glaring at her – what a surprise!
She began to cough.
“OK, Bears, I’m off !”
“This is PRIVATE PROPERTY!” roared big Daddy Bear.
“Y ou lot! Y ou think everything in this world is free to share!”
She ran and she ran through the private wood
As fast as she could!
Later she grew up to be a very sharp writer –
And a freedom fighter! 
I THINK YOU’D LIKE HER!""",
"""They love their Grandpa Nathi.But Grandpa Nathi is very sick in the 
hospital. His eyes are closed. 
The machine next to Grandpa Nathi 
goes beep, beep, beep.
 
“Mommy, why won’t Grandpa Nathi 
sing with me?” asks Thembi. 
Mommy says, “Grandpa Nathi can still 
hear you. His heart is singing with you.”BeepBeepBeepAt home, Thembi and Thulani  
are waiting at the window.
Mommy and Daddy are taking  
so long at the hospital.
Then Thembi sees Mommy and  
Daddy walk up the driveway. 
“They are back!”Mommy and Daddy are very sad. 
“What’s wrong?” asks Thembi. 
Her tummy feels sore.
Mommy’s voice is very quiet. 
“Grandpa Nathi was old and sick.  
The doctors couldn’t make him better.” 
Her eyes fill with tears, “we won’t be 
seeing Grandpa Nathi again.”Thulani is sitting outside under 
Grandpa Nathi’s favourite tree.
He doesn’t feel like playing with  
Thembi. He wishes Grandpa Nathi  
could read him a story.Thembi is angry and throws her doll. 
“Why did Grandpa Nathi have to die!”
Mommy pulls Thembi close on her lap. 
“It’s okay to be angry,” says Mommy. 
“I miss Grandpa Nathi, too.”Today Mommy, Daddy, Thulani and Thembi 
are wearing their best clothes to go to 
church for Grandpa Nathi’s funeral. 
Everyone is coming to remember Grandpa.Mommy holds Thembi’s hand as they 
sing Grandpa Nathi’s favourite songs.
Everybody sings and dances too.Thembi can’t sleep. She calls out to Mommy.
“Mommy, I miss Grandpa. My heart is so sore!”Thembi and Thulani are eating  
breakfast when Daddy walks in with  
a big, big, big cardboard tree.
“This is a memory tree,” says Daddy. 
He sticks the cardboard tree on the wall. 
Mommy has a box of photos. “Take your  
favourite pictures of Grandpa Nathi  
and stick them on the tree.”Together they all stick pictures  
of Grandpa Nathi onto the tree. They  
remember the fun times they had.
Thembi claps excitedly.
“This is my new favourite tree!”Daddy smiles. “Now anytime we 
want to remember Grandpa Nathi,  
we can come to our memory tree.”
“We will never forget Grandpa Nathi.  """,
"""I wonder what my Cat
does...
When I am at school all day?I wonder What my cat
does when I'm at
school,
I bet it is something
really cool.
Does he pound,
mix, and bake,
bread, pastry, or
a cake?
Does he cut,
thread, or knit,
a beautiful new
outft?
Does he splash
paint on it all,
pretty colours for
the wall?Does he sing,
hum, or play,
does he get
carried away?Does he conjure
real quick,
a fun magic trick?Does he tend,
feed, or sow,
a fower to grow?Does he catch a
ball on a whim,
or does it fall and
catch him?
Does he help Mum
with the chores,
or does he fnd
that just bores?Does he hit, drive,
and swing,
or is golf not his
thing?Does he talk 
on his phone, 
so he's never
alone?Does he fght fres,
save lives,
so every child,
woman, man, thrives?29Does he chill to
some tunes, 
in one of his
favourite rooms?31Or does he simply
meander and think,
with a nice coffee
to drink?Whatever my cat does,
I'm sure he does it well,
since he is awesome,
can't you tell.Cool Cat!""",
"""That frightful night, 
full of delight; 
They decided it would be fun, 
to sing, joke, and pun;
Instead of being scary and bad,  
they would be frightfully mad.
The friendly, frightful crew;
Now loved to spread glee 
and laughter, too.
They sang and danced by the  
moonlight bright;
Making the Halloween night a  
cheerful sight.
There was a vampire, 
tall and thin;
Who loved to 
play his violin.
A mummy with bandages, all  
unraveled;
Told jokes that left everyone  
happily baffed.
A friendly grey bat,
fapping his wings;
Enjoys the fun,
as everyone sings.
A friendly witch, 
with a big black hat;
Brewed potions that made  
everyone chat.
And a sweet little ghost,
striped and round;
Giggled and foated, 
fun he had found.
Grim took delight, 
in not giving a fright;
But instead with a wave, 
candies he gave.  
The haunted house, once gloomy,  
cobwebbed, and scary;
Was transformed to a pumpkin  
cottage, by a halloween fairy.
They invited children far and wide,  
for them to meet;
And bring trick or treat bags to 
fll loot so sweet.
Happy Halloween
Together they celebrated, far from  
being scary;
A Halloween flled with joy,
 oh so merry!
So in this story, you'll come to see;
That even monsters and witches  
can be as friendly as can be.""",
"""What is Elephant
doing, 
can you guess?Elephant, naughty Elephant, 
what are you doing?Why, I'm playing in the
fower bed, 
under the bright sun. Elephant, naughty Elephant, 
what are you doing?Why, I'm walking in the
village, 
nearby the homes of people.Elephant, naughty Elephant, 
what are you doing?Why I'm having a shower, 
under the cool water. Elephant, naughty Elephant, 
what are you doing?Why I'm on my way home, 
It's getting late now. Elephant, naughty Elephant, 
what are you doing?Why I'm getting ready for
bed, 
the sun is going down. Elephant, naughty Elephant, 
what are you doing?Why I'm saying good bye and
good night, 
sleep tight!Do you think
Elephant was
naughty or nice?""",
"""Colin Cow says:
Reduce!
Reuse!
Recycle!
Gerty Goat says:
Always put
your trash 
in a bin!
Patty Penguin says:
Save 
water and
electricity.
Wally Walrus says:
Reduce your
carbon
footprint!
Use a bicycle, public transport, or walk.
Peter Panda says:
Use renewable
energy.
 Harry Hippo says:
Buy products
that can be
recycled.
Morris Moose says:
Plant an
indigenous tree!
*”indigenous” means native, these types will grow better in
their natural environment. 
Baba Bear says:
Support
sustainable
practices!
Make sure we all still have fsh.
 Carly Cat says:
Don't waste 
natural 
Resources. 
 And Zenna Zebra says:
Save the Planet!
We only have
ONE.""",
"""Sacré bleu!I’m Professor Blue.
Do you?
Give me a big blue sky.  
Blue! Blue! Blue!
What do you reckon?Bah! I don’t like that colour!That’s better! Much, much better!I like to walk the beach.
What about you?
It’s got to be a blue flag 
beach, of course.The sea! Such a delightful colour!How perfectly gorgeous!I have a Kerry blue terrier .
His name is Blue.
He’s as old as the hills.My favourite flowers? 
Bluebells of course.I’m mad about blue cheese .I sing the Blues  every night.My favourite film? 
The Blue Angel , what else!My favourite poem? Blue Bird  by Han Ha-Un:
‘When I die, I’ll be a blue bird
Flying about in a blue sky, above the blue fields
Singing blue songs and weeping blue tears.’Nighty night, Bluebeard !I have blue dreams …One morning…Blue flies!What’s that terrible racket?What’s wrong with you all?
We’re blue in the face  telling you …
Blue! Blue! Blue! 
Blue! Blue! Blue!Better. Much, much better! END“Professor Blue? You’re kidding me, right?”                                                             
“Professor Blue? He ain’t no professor. No, siree!”
“Professor Blue? I’d stay well away from him 
if I were you!”""",
"""Molly’s storyMolly’s mommylovedplaying in the sandboxwith her.
At times, Molly’s mommyhad tosit back and rest while Molly
played in the sand.
One day, mommy stopped
coming to the sandbox with
Molly.
Mommyhad to stay home andrest. Molly’s dad said that her
lungs were tired and that made
mommy sleepy.
Molly liked to watch her mommysleep. She didn’t seem so tired
when she slept.
But Molly wished she couldplay with her mommy like
before.
One day, mommy anddaddysat down with Molly and told
her they had a surprise.
This news made Molly happy. She
really wanted her old mommy back.
“When are you going to thehospitalto get the operation, mommy?”They told Molly that mommy was
going to get an operation that would
help her not be so tired and sleepy allthe time.
“Well Molly,”Daddysaid,“that’s the thing.mommy doesn’t know
exactly when she will
go.”
“But how can that be?”askedMolly.
She wondered why mommy
couldn’t get better right away!
“You seeMolly, mommy hasto wait for a phone call
telling her there are new
lungs for her.”
“What new lungs? What’s thematter with her old lungs? I
thought they were going to
make her better.”
Mommy’s old lungs were notworking properly anymore.
Molly’s dad said that mommy
could not breathe with her old
lungs. She needed new ones.
Then, she would stop coughing
and wearing oxygen tubing.
“Oh,WOW, do they growher new ones?”
Growinglungs in
the
garden?
“No Molly. Someonedonates their lungs to her.”
Molly knew enough about thebody to know that you only
have one pair of lungs, and
you could not give them away
without dying. That madeMolly sad.
Molly wanted to ask who thisperson was but her dad jumped in
before she had a chance. “Wedon’t know this person and they don’t know us.”“You see Molly, a person who has
died had already decided to give
their lungs to someone like mommy
who is very sick,” dad said.
“We don’t know when thiswill happen; that is why
we don’t know when
mommy will get her new
lungs.”
It was hard for Molly to wait,but one day her mommy went
into the hospital to get her
gift of new lungs.
Shecame homefeeling much better!
Now Molly can play withher mommy in the sandbox
as before, just like she
always wanted.""",
"""One night, Fox told her kits a bedtime story.
It was the tale of a fox. This fox wanted to fly.
Her kits said they wanted to fly. They said,
“Flying looks like fun!”  Let's listen to Fox tell
the story.
Once upon a time, there was a fox. This fox
lived in the forest. She lived in a big rock den.
The den was blue. It had many pink flowers
inside.
This fox wanted to fly. She saw birds flap
their wings. The birds could fly. What fun it
must be to fly!
She went outside her rock den. She flapped
her arms. She did not fly.
Just then, a bird came by. This is who the fox
wanted to talk to. Birds know how to fly. The
fox yelled, “Bird, please stop!”.
The bird sat in a tree. The fox said, “I want to
fly like you.” The bird said, “Flying is easy.
Just flap your wings. But, I have never seen a
fox fly.” Having said that, the bird flew away.
Fox flapped her arms faster this time. She did
not fly.
In the tree was a beehive. This is who the fox
wanted to talk to. Bees know how to fly.
Maybe the bees can teach her how to fly.
The fox yelled, “Bees, please come out!”. The
bees came out of the beehive. The fox said, “I
want to fly like you.” One bee said, “Flying is
easy.” Another bee said, “Just flap your
wings.” A third bee said, “But, I have never
seen a fox fly.” Having said that, the bees
went in the beehive.
The fox  flapped her arms even faster this
time . She still did not fly. She was not very
happy.
She walked for a long time. It was now dark.
Soon, she saw a bat. The fox thought,
“Maybe, the bat can help me. She looks like
me and she has wings”
The fox said, “Bat, I want to fly like you.”  The
bat said, “I love to fly. I just flap my wings and
I fly. Flying is easy.  I can fly fast. I catch bugs
for my dinner.”  The fox asked, “Have you
ever seen a fox fly.”
The bat said, “Yes, I have. Flying foxes live in
trees near the river. They look like you and
me. They can fly.” Having said that, the bat
left.
The fox went to the river. She looked up in
the trees. There was a flying fox. The flying
fox was sleeping. It was hanging from a tree
branch.
The flying fox heard the fox walking in the
grass. She woke up and looked at the fox.
She had never seen a fox before.
The flying fox said, “Hello, how can I help
you?” The fox said. “I want to fly like you do.”
The flying fox said, “You do look like me.
Maybe you can fly. I think you need wings.
Then maybe you can fly.” The fox said,
“Thank you.” and left quickly.
On the way home, she found some cloth. It
was  a flag that blew away from the town.
She took the flag home. She would make
some wings.
At home, she cut the flag. She sewed the
flag. Soon, she had wings. She put the wings
on.
She went outside and flapped her new wings.
She dreamed she was flying.
Mother fox said, “That is the story. Did you
like it?” The kits said, “Yes, Did the fox really
fly,  Momma?” She said, “Maybe, do you two
think she did?”
Do you think the fox could fly?""",
"""!! PSST !!
4There's a
    MONSTER!!!
5s
There's a Monster in my
house...
6Zzzzz....Zzz
…..HEHEHe
HeheheheShe likes to hide under
my bed...
I know this for sure:
Sometimes I hear her
laughing,
Sometimes I hear her snore!
7s
There's a Monster in my
house...
8She likes to hide in my
closet...
This is very clear:
She mixes up all my socks,
And eats my underwear!
9There's a Monster in my
house...
10She likes to hide under the
table....
I know this as a fact:
She messes up my
homework,
And makes it less exact!
11s
There's a Monster in my
house...
12She likes to
hide behind
the
curtain.....
I know this
for real:
She secretly eats my candy,
And cookies, her favourite
meal!
13s
There's a Monster in my
house...
14She likes to hide in my
bedroom....
I know this for certain:
She plays with my tea set;
15And invites me once
again :-)
16There's a Monster in my
house...
17PSST!!
18My underwear is missing...
My candy and cookies are
gone...
My homework is all wrong...
19!!! BUT !!!
20…tea is always for
two...
She is my friend and I
wouldn't have it any
other way!
21Would you like
some tea too?""",
"""“Look,” Nali says.
“There’s Mum.”“When I grow up, I want
to be a police o fficer, too.
Like Mum!”“I want to be a barber,
like Dad,” Elina says.“I like ﬂowers,” Nali says.
“I could also sell ﬂowers
when I grow up.”“I could also become a bus
driver,” says Elina.“Oh, I like ice-cream,” Nali
says. “Imagine selling
ice-cream all day!”“I want to learn how
to cook,” Elina says.
“Like Grandma?”
“Yes!” “I want to learn how to read,”
says Nali.
Elina grabs a book.
“Let me read for
you,” she says.""",
"""I feel -
Sad
When someone
hurts me :-(
45
I feel -
Anxious
When I'm about to
try something
new :-0
67
I feel -
Shy
When I'm around
someone
new or special :- §
89
I feel -
Scared
When I'm about to
do something
diffcult :-O
1011
I feel -
Angry
When something
happens I don't
like  :-[]
1213
I feel -
Happy
When something
happens I like :-)
1415
I feel -
Happy
When I SHARE
with someone
Like you! :-)""",
"""Now, her ears areyellow.
Now, her tummy isbrown.
Now, her mouth isred.
Now, her hands areblue.
Now, her back isgreen.
Now, her legs are pink.
Now, Bear is colourful!
Oh no! Where did all her colours go?""",
"""Relax and lie with your head back in thewater with your ears submerged.
Take deep breaths to help with buoyancy.
Lift your feet, while extending your armsto the side.
Try and keep a starfish shape.
Sculling can also help support you to stayafloat.
1.2.3.4.5.""",
]

# File path to save the JSON file
json_title_path = 'story_titles.json'
json_content_path = 'story_content.json'

# Remove leading/trailing whitespace including new lines
story_titles_cleaned = [title.strip() for title in story_titles]
story_content_cleaned = [story.replace('\n',' ') for story in story_content]

# Creating a dictionary with the story titles and content
data_title = {"titles": story_titles_cleaned}
data_content = {"content": story_content_cleaned}

# Writing the data to a JSON file
with open(json_title_path, 'w') as json_file:
    json.dump(data_title, json_file, indent=4)

with open(json_content_path, 'w') as json_file2:
    json.dump(data_content, json_file2, indent=4)

subprocess.run(["python", "clean_content_data.py"])