from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item

engine = create_engine('sqlite:///categoryItem.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

category1 = Category(name="Soccer", user_id=1)

session.add(category1)
session.commit()

Item1 = Item(name="Soccer cleats", description="Football boots, called cleats or soccer shoes in North America, are an item of footwear worn when playing football. Those designed for grass pitches have studs on the outsole to aid grip.",
                        user_id=1, category=category1)

session.add(Item1)
session.commit()


Item2 = Item(name="Shin guard", description="A shin guard or shin pad is a piece of equipment worn on the front of a player's shin to protect it from injury.",
                        user_id=1, category=category1)

session.add(Item2)
session.commit()

Item3 = Item(name="Soccer ball", description="A football, soccer-ball, or association football ball is the ball used in the sport of association football. The name of the ball varies according to whether the sport is called football, soccer, or association football. The ball's spherical shape, as well as its size, weight, and material composition, are specified by Law 2 of the Laws of the Game maintained by the International Football Association Board.   Additional, more stringent, standards are specified by FIFA and subordinate governing bodies for the balls used in the competitions they sanction.",
                        user_id=1, category=category1)

session.add(Item3)
session.commit()

Item4 = Item(name="Jersey", description="A jersey is an item of knitted clothing, traditionally in wool or cotton, with sleeves, worn as a pullover, as it does not open at the front, unlike a cardigan. The shirts now commonly worn by sports teams as part of the team uniform are also referred to as jerseys, although they bear little resemblance to the original hand-kitted woolen garments.",
                        user_id=1, category=category1)

session.add(Item4)
session.commit()

Item5 = Item(name="Soccer Pitch", description="A football pitch (also known as a football field or soccer field) is the playing surface for the game of association football. Its dimensions and markings are defined by Law 1 of the Laws of the Game. The surface can either be natural or artificial. Artificial surfaces must be green in colour. The pitch is typically made of turf (grass) or artificial turf, although amateur and recreational teams often play on dirt fields.",
                        user_id=1, category=category1)

session.add(Item5)
session.commit()

category2 = Category(name="Basketball", user_id=1)

session.add(category2)
session.commit()


Item1 = Item(name="Basketball", description="A basketball is a spherical ball used in basketball games. Basketballs typically range in size from very small promotional items only a few inches in diameter to extra large balls nearly a foot in diameter used in training exercises.",
                        user_id=1, category=category2)

session.add(Item1)
session.commit()

Item2 = Item(name="Basketball backboard", description="A backboard is a piece of basketball equipment. It is a raised vertical board with an attached basket consisting of a net suspended from a hoop. It is made of a flat, rigid piece of, often Plexiglas or tempered glass which also has the properties of safety glass when accidentally shattered.",
                        user_id=1, category=category2)

session.add(Item2)
session.commit()

Item3 = Item(name="Jersey", description="A jersey is an item of knitted clothing, traditionally in wool or cotton, with sleeves, worn as a pullover, as it does not open at the front, unlike a cardigan. The shirts now commonly worn by sports teams as part of the team uniform are also referred to as jerseys, although they bear little resemblance to the original hand-kitted woolen garments.",
                        user_id=1, category=category2)

session.add(Item3)
session.commit()

Item4 = Item(name="Basketball Court", description="In basketball, the basketball court is the playing surface, consisting of a rectangular floor, with baskets at each end. In professional or organized basketball, especially when played indoors, it is usually made out of a wood, often maple, and highly polished and completed with a 10 foot rim. Outdoor surfaces are generally made from standard paving materials such as concrete or asphalt.",
                        user_id=1, category=category2)

session.add(Item4)
session.commit()

category1 = Category(name="Baseball", user_id=1)

session.add(category1)
session.commit()


Item1 = Item(name="Baseball bat", description="A baseball bat is a smooth wooden or metal club used in the sport of baseball to hit the ball after it is thrown by the pitcher.",
                        user_id=1, category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="Baseball", description="A baseball is a ball used in the sport of the same name. The ball features a rubber or cork center, wrapped in yarn, and covered, in the words of the Official Baseball Rules with two strips of white horsehide or cowhide, tightly stitched together.",
                        user_id=1, category=category1)

session.add(Item2)
session.commit()

Item3 = Item(name="Baseball Glove", description="A baseball glove or mitt is a large leather glove worn by baseball players of the defending team, which assists players in catching and fielding balls hit by a batter or thrown by a teammate.",
                        user_id=1, category=category1)

session.add(Item3)
session.commit()

Item4 = Item(name="Batting Helmet", description="A batting helmet is worn by batters in the game of baseball or softball. It is meant to protect the batter's head from errant pitches thrown by the pitcher.",
                        user_id=1, category=category1)

session.add(Item4)
session.commit()

category1 = Category(name="Cricket", user_id=1)

session.add(category1)
session.commit()


Item1 = Item(name="Cricket Bat", description="A cricket bat is a specialised piece of equipment used by batsmen in the sport of cricket to hit the ball, typically consisting of a cane handle attached to a flat-fronted willow-wood blade. ",
                        user_id=1, category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="Cricket Ball", description="A cricket ball is a hard, solid ball used to play cricket.  A cricket ball consists of cork covered by leather, and manufacture is regulated by cricket law at first-class level. ",
                        user_id=1, category=category1)

session.add(Item2)
session.commit()

Item3 = Item(name="Cricket Pitch", description="In the game of cricket, the cricket pitch consists of the central strip of the cricket field between the wickets. It is 22 yards (20.12 m) long and 10 feet (3.05 m) wide. The surface is flat and normally covered with extremely short grass though this grass is soon removed by wear at the ends of the pitch.",
                        user_id=1, category=category1)

session.add(Item3)
session.commit()

Item4 = Item(name="Cricket Stumps", description="In cricket, the stumps are the three vertical posts that support the bails and form the wicket. Stumping or being stumped is a method of dismissing a batsman.",
                        user_id=1, category=category1)

session.add(Item4)
session.commit()

category1 = Category(name="Ice Hockey", user_id=1)

session.add(category1)
session.commit()


Item1 = Item(name="Hockey Stick", description="An ice hockey stick is a piece of equipment used in ice hockey to shoot, pass, and carry the puck across the ice.",
                        user_id=1, category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="Ice Skates", description="Ice skates are metal blades attached underfoot and used to propel the bearer across a sheet of ice while ice skating.",
                        user_id=1, category=category1)

session.add(Item2)
session.commit()

Item3 = Item(name="Puck", description="A hockey puck is a disk made of vulcanized rubber that serves the same functions in various games as a ball does in ball games. The best-known use of pucks is in ice hockey, a major international sport.",
                        user_id=1, category=category1)

session.add(Item3)
session.commit()

category1 = Category(name="Snowboarding", user_id=1)

session.add(category1)
session.commit()


Item1 = Item(name="Googles", description="Goggles, or safety glasses, are forms of protective eyewear that usually enclose or protect the area surrounding the eye in order to prevent particulates, water or chemicals from striking the eyes.",
                        user_id=1, category=category1)

session.add(Item1)
session.commit()

Item2 = Item(name="Snowboard", description="Snowboards are boards where both feet are secured to the same board, which are wider than skis, with the ability to glide on snow. Snowboards widths are between 6 and 12 inches or 15 to 30 centimeters.",
                        user_id=1, category=category1)

session.add(Item2)
session.commit()

print "added menu items!"
