from tips.models import Tip
from recipes.models import Recipe
from store.models import Product    
recipes = [
    {
        'name': 'Scrambled Eggs',
        'description': 'Classic breakfast dish with fluffy scrambled eggs.',
        'image': '/images/recipe1.jpg',
        'ingredients': '2 large eggs, Salt, Pepper, 1 tablespoon butter or cooking oil',
        'instructions': '1. Crack the eggs and whisk., 2. Season with salt and pepper., 3. Heat skillet with butter/oil., 4. Pour eggs and cook., 5. Stir and scramble until desired consistency., 6. Serve hot.'
    },
    {
        'name': 'Caprese Salad',
        'description': 'Simple salad with tomatoes, fresh mozzarella, and basil.',
        'image': '/images/recipe2.jpg',
        'ingredients': 'Tomatoes, Fresh mozzarella cheese, Fresh basil leaves, Balsamic glaze, Olive oil, Salt, Pepper',
        'instructions': '1. Slice tomatoes and fresh mozzarella., 2. Arrange slices on a plate., 3. Tuck fresh basil leaves between tomato and mozzarella slices., 4. Drizzle with balsamic glaze and olive oil., 5. Serve immediately. '
    },
    {
        'name': 'Grilled Cheese Sandwich',
        'description': 'Classic comfort food with gooey melted cheese and crispy bread.',
        'image': '/images/recipe3.jpg',
        'ingredients': '2 slices of bread, Butter, 2 slices of cheese',
        'instructions': '1. Butter one side of each bread slice., 2. Place cheese slices between bread slices., 3. Cook in a skillet until golden brown., 4. Flip and cook the other side., 5. Remove from heat and serve warm.'
    },
    {
        'name': 'Fruit Yogurt Parfait',
        'description': 'A healthy and delicious layered dessert with yogurt and fresh fruits.',
        'image': '/images/recipe4.jpeg',
        'ingredients': '1 cup plain yogurt, 1 cup mixed fresh fruits, 2 tablespoons honey or maple syrup, Granola or nuts for topping',
        'instructions': '1. Spoon a layer of yogurt in a glass or bowl., 2. Add a layer of mixed fresh fruits., 3. Repeat layers until finished., 4. Drizzle with honey or maple syrup., 5. Top with granola or nuts., 6. Serve immediately.'
    },
    {
        'name': 'Pasta Aglio e Olio',
        'description': 'A simple and flavorful Italian pasta dish with garlic and olive oil.',
        'image': '/images/recipe5.jpg',
        'ingredients': '8 ounces spaghetti or linguine pasta, 4 cloves garlic, 1/4 cup extra virgin olive oil, Red pepper flakes, Salt, Pepper, Fresh parsley',
        'instructions': '1. Cook pasta until al dente., 2. Sauté sliced garlic and red pepper flakes in olive oil., 3. Add cooked pasta to the skillet., 4. Season with salt and pepper., 5. Remove from heat., 6. Sprinkle with fresh parsley., 7. Serve hot.'
    },
    {
        'name': 'Spaghetti Bolognese',
        'description': 'Classic Italian pasta dish with meaty Bolognese sauce.',
        'image': '/images/recipe6.jpg',
        'ingredients': '400g ground beef, 1 onion, 2 cloves garlic, 400g canned tomatoes, 2 tablespoons tomato paste, 1 teaspoon dried oregano, Salt, Pepper, 300g spaghetti',
        'instructions': '1. Cook spaghetti according to package instructions., 2. In a skillet cook ground beef until browned., 3. Add chopped onion and garlic, cook until softened., 4. Stir in canned tomatoes tomato paste oregano salt and pepper., 5. Simmer for 20 minutes., 6. Serve Bolognese sauce over cooked spaghetti.'
    },
    {
        'name': 'Chicken Caesar Salad',
        'description': 'Refreshing salad with grilled chicken, crisp lettuce, and Caesar dressing.',
        'image': '/images/recipe7.jpg',
        'ingredients': '2 boneless, skinless chicken breasts, Romaine lettuce, Croutons, Parmesan cheese, Caesar dressing',
        'instructions': '1. Season chicken breasts and grill until fully cooked., 2. Chop lettuce and place in a bowl., 3. Slice grilled chicken and add to the salad., 4. Sprinkle croutons and Parmesan cheese., 5. Drizzle Caesar dressing over the salad., 6. Toss and serve.'
    },
    {
        'name': 'Margherita Pizza',
        'description': 'Classic pizza with tomato, mozzarella, and basil.',
        'image': '/images/recipe8.jpg',
        'ingredients': 'Pizza dough, Tomato sauce, Fresh mozzarella cheese, Fresh basil leaves, Olive oil',
        'instructions': '1. Preheat oven to 475°F (245°C)., 2. Roll out pizza dough., 3. Spread tomato sauce over the dough., 4. Add slices of fresh mozzarella., 5. Bake for 12-15 minutes or until crust is golden., 6. Garnish with fresh basil leaves and drizzle with olive oil.'
    },
    {
        'name': 'Chocolate Chip Cookies',
        'description': 'Classic chocolate chip cookies.',
        'image': '/images/recipe9.jpg',
        'ingredients': '1 cup butter, 3/4 cup brown sugar, 3/4 cup granulated sugar, 2 large eggs, 1 teaspoon vanilla extract, 2 1/4 cups all-purpose flour, 1 teaspoon baking soda, 1/2 teaspoon salt, 2 cups chocolate chips',
        'instructions': '1. Preheat oven to 375°F (190°C)., 2. In a bowl cream together butter brown sugar and granulated sugar., 3. Beat in eggs and vanilla., 4. In a separate bowl whisk together flour baking soda and salt., 5. Combine wet and dry ingredients., 6. Fold in chocolate chips., 7. Drop spoonfuls of dough onto a baking sheet., 8. Bake for 10-12 minutes or until edges are golden., 9. Allow to cool on a wire rack.'
    },
    {
        'name': 'Vegetable Stir-Fry',
        'description': 'Healthy stir-fry with a variety of colorful vegetables.',
        'image': '/images/recipe10.jpg',
        'ingredients': 'Broccoli, Bell peppers, Carrots, Snap peas, Soy sauce, Ginger, Garlic, Sesame oil',
        'instructions': '1. Cut vegetables into bite-sized pieces., 2. Heat sesame oil in a wok or skillet., 3. Add minced ginger and garlic., 4. Stir-fry vegetables until crisp-tender., 5. Add soy sauce for seasoning., 6. Serve hot.'
    },
    {
        'name': 'Homemade Tomato Soup',
        'description': 'Comforting tomato soup made from scratch.',
        'image': '/images/recipe11.jpg',
        'ingredients': 'Tomatoes, Onion, Garlic, Vegetable broth, Olive oil, Basil, Salt, Pepper',
        'instructions': '1. Saute chopped onion and garlic in olive oil., 2. Add chopped tomatoes and cook until soft., 3. Pour in vegetable broth and bring to a boil., 4. Simmer for 15-20 minutes., 5. Blend the soup until smooth., 6. Season with basil salt and pepper., 7. Serve hot.'
    },
    {
        'name': 'Grilled Salmon',
        'description': 'Healthy and flavorful grilled salmon fillets.',
        'image': '/images/recipe12.jpeg',
        'ingredients': 'Salmon fillets, Lemon, Olive oil, Dill, Salt, Pepper',
        'instructions': '1. Preheat grill to medium-high heat., 2. Brush salmon fillets with olive oil., 3. Squeeze lemon juice over the fillets., 4. Sprinkle with chopped dill salt and pepper., 5. Grill for 4-5 minutes per side or until cooked through., 6. Serve with lemon wedges.'
    },
    {
        'name': 'Vegetarian Tacos',
        'description': 'Delicious tacos filled with seasoned beans, veggies, and toppings.',
        'image': '/images/recipe13.jpg',
        'ingredients': 'Black beans, Corn tortillas, Avocado, Tomato, Onion, Cilantro, Lime, Taco seasoning',
        'instructions': '1. Rinse and drain black beans., 2. Season beans with taco seasoning., 3. Warm corn tortillas., 4. Fill tortillas with seasoned beans., 5. Top with diced avocado tomato onion and cilantro., 6. Squeeze lime over the tacos., 7. Enjoy!'
    },
    {
        'name': 'Mango Smoothie',
        'description': 'Refreshing smoothie with mango, yogurt, and banana.',
        'image': '/images/recipe14.jpg',
        'ingredients': 'Mango, Yogurt, Banana, Honey, Ice cubes',
        'instructions': '1. Peel and dice mango., 2. Blend mango yogurt banana honey and ice cubes until smooth., 3. Pour into a glass and enjoy!'
    },
    {
        'name': 'Chicken Tikka Masala',
        'description': 'Rich and flavorful Indian chicken curry with a creamy tomato-based sauce.',
        'image': '/images/recipe15.jpg',
        'ingredients': 'Chicken thighs, Yogurt, Garam masala, Ginger, Garlic, Tomato puree, Heavy cream, Onion, Cilantro, Basmati rice',
        'instructions': '1. Marinate chicken in yogurt, garam masala, ginger, and garlic., 2. Grill or cook chicken until fully cooked., 3. In a pan sauté chopped onion until golden., 4. Add tomato puree and cook until oil separates., 5. Stir in heavy cream and cooked chicken., 6. Simmer until the sauce thickens., 7. Garnish with chopped cilantro., 8. Serve over cooked basmati rice.'
    },
    {
        'name': 'Shrimp Scampi',
        'description': 'Garlicky shrimp served over pasta with a lemony butter sauce.',
        'image': '/images/recipe16.jpg',
        'ingredients': 'Shrimp, Linguine pasta, Butter, Olive oil, Garlic, Red pepper flakes, White wine, Lemon, Parsley, Salt, Pepper',
        'instructions': '1. Cook linguine pasta according to package instructions., 2. In a skillet melt butter with olive oil., 3. Add minced garlic and red pepper flakes., 4. Sauté shrimp until pink and opaque., 5. Pour in white wine and squeeze lemon., 6. Season with salt and pepper., 7. Toss cooked pasta in the shrimp and sauce., 8. Garnish with chopped parsley.'
    },
    {
        'name': 'Vegetarian Pad Thai',
        'description': 'Thai stir-fried noodles with tofu, vegetables, and a tangy tamarind sauce.',
        'image': '/images/recipe17.jpg',
        'ingredients': 'Rice noodles, Tofu, Bean sprouts, Carrots, Scallions, Peanuts, Eggs, Tamarind paste, Soy sauce, Lime, Sugar, Chili flakes',
        'instructions': '1. Soak rice noodles in hot water until softened., 2. In a wok stir-fry tofu carrots and scallions., 3. Push ingredients to one side and scramble eggs., 4. Add soaked rice noodles to the wok., 5. In a small bowl mix tamarind paste soy sauce lime juice sugar and chili flakes., 6. Pour sauce over the noodles and toss., 7. Garnish with bean sprouts and chopped peanuts.'
    },
    {
        'name': 'Quinoa Salad',
        'description': 'Nutritious salad with quinoa, mixed greens, veggies, and a zesty vinaigrette.',
        'image': '/images/recipe18.jpg',
        'ingredients': 'Quinoa, Mixed greens, Cherry tomatoes, Cucumber, Avocado, Red onion, Feta cheese, Olive oil, Balsamic vinegar, Dijon mustard, Honey',
        'instructions': '1. Cook quinoa according to package instructions., 2. In a large bowl combine cooked quinoa mixed greens halved cherry tomatoes sliced cucumber diced avocado sliced red onion and crumbled feta cheese., 3. In a small bowl whisk together olive oil balsamic vinegar Dijon mustard and honey to make the vinaigrette., 4. Drizzle the vinaigrette over the salad and toss to combine.'
    },
    {
        'name': 'Classic Caesar Salad',
        'description': 'Timeless Caesar salad with crisp romaine lettuce, croutons, and Caesar dressing.',
        'image': '/images/recipe19.jpg',
        'ingredients': 'Romaine lettuce, Croutons, Parmesan cheese, Caesar dressing',
        'instructions': '1. Wash and chop romaine lettuce., 2. Toss lettuce with croutons and shaved Parmesan cheese., 3. Drizzle Caesar dressing over the salad., 4. Toss until evenly coated., 5. Serve immediately.'
    },
    {
        'name': 'Mushroom Risotto',
        'description': 'Creamy Italian risotto with mushrooms and Parmesan cheese.',
        'image': '/images/recipe20.jpg',
        'ingredients': 'Arborio rice, Mushrooms, Onion, Garlic, White wine, Vegetable broth, Parmesan cheese, Butter, Olive oil',
        'instructions': '1. In a pan, sauté chopped onion and garlic in olive oil., 2. Add sliced mushrooms and cook until browned., 3. Stir in Arborio rice and cook until translucent., 4. Pour in white wine and cook until absorbed., 5. Gradually add vegetable broth, stirring continuously., 6. Continue adding broth until rice is creamy and cooked., 7. Stir in Parmesan cheese and butter., 8. Season with salt and pepper., 9. Serve hot.'
    },
    {
        'name': 'Lemon Herb Grilled Chicken',
        'description': 'Juicy grilled chicken marinated in a flavorful blend of lemon and herbs.',
        'image': '/images/recipe21.jpg',
        'ingredients': 'Chicken breasts, Lemon juice, Olive oil, Garlic, Fresh herbs (such as thyme and rosemary), Salt, Pepper',
        'instructions': '1. In a bowl mix lemon juice olive oil minced garlic chopped fresh herbs salt and pepper to create the marinade., 2. Coat chicken breasts with the marinade and let it sit for at least 30 minutes., 3. Preheat the grill., 4. Grill chicken until fully cooked, with beautiful grill marks., 5. Let it rest for a few minutes before serving.'
    },
    {
        'name': 'Homemade Guacamole',
        'description': 'Fresh and flavorful guacamole made with ripe avocados, tomatoes, onions, and lime.',
        'image': '/images/recipe22.jpg',
        'ingredients': 'Ripe avocados, Tomatoes, Red onion, Lime, Garlic, Jalapeño, Cilantro, Salt',
        'instructions': '1. Cut avocados in half remove the pit and scoop the flesh into a bowl., 2. Mash the avocados with a fork., 3. Dice tomatoes finely chop red onion mince garlic and finely chop jalapeño. Add them to the bowl., 4. Squeeze lime juice over the mixture., 5. Stir in chopped cilantro and season with salt to taste'
    }
]


for recipe_data in recipes:
    try:
        Recipe.objects.create(
            name=recipe_data['name'],
            description=recipe_data['description'],
            image=recipe_data['image'],
            ingredients=recipe_data['ingredients'],
            instructions=recipe_data['instructions'],
        )
    except Exception as e:
        print("Error creating recipe:", e)

tip1 = Tip.objects.create(user=None,subject="Flavorful Stir-Fry Creations",description="Cooking the perfect stir-fry involves more than just tossing ingredients in a hot pan. Start by preparing all your ingredients beforehand, ensuring that everything is chopped and ready to go. Use a wok or a wide skillet with high sides to allow for efficient tossing and even cooking. Begin by stir-frying aromatics like garlic and ginger in hot oil to infuse the base flavors. Add proteins next, such as thinly sliced chicken or beef, and cook until golden brown. Incorporate a colorful array of vegetables, starting with those that require more cooking time and gradually adding quicker-cooking veggies. For an authentic touch, whip up a simple sauce with soy sauce, oyster sauce, and a hint of sweetness. Toss everything together until well-coated, and finish with a sprinkle of fresh herbs or sesame seeds for that perfect stir-fry sensation.",image=None)
tip1.save()
tip2 = Tip.objects.create(user=None,subject="Homemade Pizza Mastery",description="Elevate your pizza-making skills with a few insider tips. Begin by selecting high-quality pizza dough or, better yet, try making your own for an authentic touch. Allow the dough to rest and rise properly for that perfect crust. Preheat your oven as high as it goes, ideally around 500°F (260°C), to achieve that coveted crispy crust. Dust your work surface generously with flour to prevent sticking as you roll out the dough to your desired thickness. For a flavorful base, consider using a homemade tomato sauce or a blend of olive oil and garlic. When it comes to toppings, the possibilities are endless—experiment with fresh mozzarella, a variety of cheeses, and an assortment of veggies and meats. Don't forget to sprinkle a pinch of sea salt over the top before baking to enhance the flavors. Keep a close eye on your pizza in the oven, and once it's golden and bubbling, pull it out, let it cool for a moment, and savor the fruits of your pizza-making prowess.",image=None)
tip2.save()
tip3 = Tip.objects.create(user=None,subject="Slow-Cooked Comfort: Hearty Beef Stew",description="There's something magical about the aroma of a simmering beef stew wafting through the kitchen on a chilly day. Crafting the perfect hearty beef stew is an art that requires time and patience. Start by choosing a well-marbled cut of beef, like chuck or stew meat, and generously season it with salt and pepper. In a large pot, heat oil over medium-high heat and sear the beef until it develops a deep, golden-brown crust. Set the beef aside and sauté a mirepoix of onions, carrots, and celery in the flavorful remnants of the beef. Deglaze the pot with a hearty red wine, scraping up the delicious brown bits from the bottom. Return the beef to the pot along with beef broth, tomatoes, and a bouquet garni of fresh herbs. Bring the stew to a gentle simmer, cover, and let it work its magic for a few hours. The slow-cooking process allows the beef to become tender, and the flavors to meld into a rich, comforting broth. As a finishing touch, add a medley of root vegetables like potatoes and parsnips, letting them cook until fork-tender. Ladle the stew into bowls, garnish with a sprinkle of fresh parsley, and serve with crusty bread to soak up every last bit of goodness. This slow-cooked masterpiece is sure to warm both body and soul.",image=None)
tip3.save()

 
product1 = Product.objects.create(name="Khobar 10-Piece Stainless Steel Cookware Set",description="Consisting of assorted cooking vessels, this ten-piece cookware set is a must-have for your kitchen. Made from stainless steel material,these durable pieces are food safe and easy to use. The set comes with sleek handles that ensure maximum safety when cooking.",price=33.68,image="\images\item1.webp")

product2 = Product.objects.create(name="Bake It 12-Cup Carbon Steel Muffin Pan - 27x35 cm",description="Bake delicious muffins at home with this tray in your collection. The muffin pan is made from durable carbon steel with provisions to make a dozen muffins at a time. The baking tray has a non-stick finish for added convenience.",price=2.40,image="\images\item2.webp")

product3 = Product.objects.create(name="Tuile Stainless Steel Whistling Kettle - 3 L",description="A nifty pick for your kitchen, this kettle is ideal for boiling water to make hot beverages. Made from stainless steel, the piece is topped with a circular lid. Designed with a curved handle, this whistling kettle is a modern addition to your home. You can also consider this as a gifting option for new homes.",price=7.50,image="\images\item3.webp")

product4 = Product.objects.create(name="Decatur Carbon Steel Springform Cake Pan - 26 cm",description="Bake your favourite cakes at home with this cake pan in your cookware essentials. The round cake pan is made from carbon steel with a non-stick finish for added ease. The two-piece cake pan requires a thorough hand wash after each use for its efficient care.",price=2.93,image="\images\item4.webp")

product5 = Product.objects.create(name="Essential 8-Piece Measuring Spoon and Cup Set",description="Go for a smart look as you notch up your kitchen essentials with this set of measuring cups and spoons. The cups and spoons are handy and boast a modern appeal. Food-safe and dishwasher-safe, the set is made of stainless steel and plastic and are apt for regular use.",price=1.20,image="\images\item5.webp")

product6 = Product.objects.create(name="Bake It 3-Piece Flower Shaped Cookie Cutter",description="Curated from quality material, this cookie cutter is perfect for the baker in you. With various sizes, this flower-shaped three-piece set will make baking a fun experience for you.",price=0.53,image="\images\item6.webp")

product7 = Product.objects.create(name="Bake It Wavy Pastry Cutter",description="Ensure an easy way to cut your pastries after baking with this cutter. A handy pick, this cutter is designed with a wavy blade and an easy-to-grip handle.",price=1.13,image="\images\item7.webp")

product8 = Product.objects.create(name="Bake It Solid Spoon",description="A spoon that flaunts a neat design and can be used to pick on solid food items or soups and curries for your convenience. It has a matte finish and is dishwasher safe.",price=1.58,image="\images\item8.webp")

product9 = Product.objects.create(name="Bake It Stainless Steel Rolling Pin",description="Made from stainless steel, this durable rolling pin is a modern and convenient pick for your kitchen. Get a hassle-free cooking experience with the help of this food-safe rolling pin that's flanked by contrast handles. Ideal for flattening out the dough, this piece can be hand washed whenever needed.",price=3.38,image="\images\item9.webp")    