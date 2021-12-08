from models import User, Post, Tag, PostTag, db 
from app import app

db.drop_all()
db.create_all()

#If User table isn't empty, empty it
User.query.delete()

#Add users
aubrey = User(first_name='Aubrey', last_name='Selamu-Bell')
olani = User(first_name='Olani', last_name='Selamu')
yohanna = User(first_name='Yohanna', last_name='Selamu')

#Add new objects to session
db.session.add(aubrey)
db.session.add(olani)
db.session.add(yohanna)

#Commit to session
db.session.commit()

#******************************************************
#Post Model

#If Post table isn't empty, empty it
Post.query.delete()

#Add posts
engineering = Post(title='Finally secured a software engineering role', content='After several months of hard work, I have finally accepted a job offer from one of the top tech companies in the world! I am exctied for this new transition in my life!', user_id = 1 )
soccer = Post(title='Machester United wins the Champions League!', content='After many years, Manchester United has finally returned as the best team in Europe!', user_id=2)
fish = Post(title = 'Fishing in Homosassa, FL', content='My first fishing experience was in Homosassa, FL and that was the day I fell in love with fishing! I caught a couple of groupers, redfish and almost caught a shark!', user_id=3)

#Add new objects to session
db.session.add(engineering)
db.session.add(soccer)
db.session.add(fish)

#Commit to session
db.session.commit()

#********************************************************
#Tag Model

#If tags table isn't empty, empty it
Tag.query.delete()

#Add posts
software_tag = Tag(name='software engineering')
soccer_tag = Tag(name='soccer')
fish_tag = Tag(name='fishing')

#Add new objects to session
db.session.add(software_tag)
db.session.add(soccer_tag)
db.session.add(fish_tag)

#Commit to session
db.session.commit()

#********************************************************
#PostTag Model

#If tags table isn't empty, empty it
PostTag.query.delete()

#Add posts
software_pt = PostTag(post_id=1, tag_id=1)
soccer_pt = PostTag(post_id=2, tag_id=2)
fish_pt = PostTag(post_id=3, tag_id=3)

#Add new objects to session
db.session.add(software_pt)
db.session.add(soccer_pt)
db.session.add(fish_pt)

#Commit to session
db.session.commit()