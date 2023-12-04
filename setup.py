# Assuming you have a Recipe model in your Django application
from recipes.models import Recipe

# Creating 10 Recipe objects
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
        'name': 'Spaghetti Bolognese',
        'description': 'Classic Italian pasta dish with meaty Bolognese sauce.',
        'image': '/images/spaghetti_bolognese.jpg',
        'ingredients': '400g ground beef, 1 onion, 2 cloves garlic, 400g canned tomatoes, 2 tablespoons tomato paste, 1 teaspoon dried oregano, Salt, Pepper, 300g spaghetti',
        'instructions': '1. Cook spaghetti according to package instructions., 2. In a skillet, cook ground beef until browned., 3. Add chopped onion and garlic, cook until softened., 4. Stir in canned tomatoes, tomato paste, oregano, salt, and pepper., 5. Simmer for 20 minutes., 6. Serve Bolognese sauce over cooked spaghetti.'
    },
    {
        'name': 'Chicken Caesar Salad',
        'description': 'Refreshing salad with grilled chicken, crisp lettuce, and Caesar dressing.',
        'image': '/images/chicken_caesar_salad.jpg',
        'ingredients': '2 boneless, skinless chicken breasts, Romaine lettuce, Croutons, Parmesan cheese, Caesar dressing',
        'instructions': '1. Season chicken breasts and grill until fully cooked., 2. Chop lettuce and place in a bowl., 3. Slice grilled chicken and add to the salad., 4. Sprinkle croutons and Parmesan cheese., 5. Drizzle Caesar dressing over the salad., 6. Toss and serve.'
    },
    {
        'name': 'Margherita Pizza',
        'description': 'Classic pizza with tomato, mozzarella, and basil.',
        'image': '/images/margherita_pizza.jpg',
        'ingredients': 'Pizza dough, Tomato sauce, Fresh mozzarella cheese, Fresh basil leaves, Olive oil',
        'instructions': '1. Preheat oven to 475°F (245°C)., 2. Roll out pizza dough., 3. Spread tomato sauce over the dough., 4. Add slices of fresh mozzarella., 5. Bake for 12-15 minutes or until crust is golden., 6. Garnish with fresh basil leaves and drizzle with olive oil.'
    },
    {
        'name': 'Chocolate Chip Cookies',
        'description': 'Classic chocolate chip cookies.',
        'image': '/images/chocolate_chip_cookies.jpg',
        'ingredients': '1 cup butter, 3/4 cup brown sugar, 3/4 cup granulated sugar, 2 large eggs, 1 teaspoon vanilla extract, 2 1/4 cups all-purpose flour, 1 teaspoon baking soda, 1/2 teaspoon salt, 2 cups chocolate chips',
        'instructions': '1. Preheat oven to 375°F (190°C)., 2. In a bowl, cream together butter, brown sugar, and granulated sugar., 3. Beat in eggs and vanilla., 4. In a separate bowl, whisk together flour, baking soda, and salt., 5. Combine wet and dry ingredients., 6. Fold in chocolate chips., 7. Drop spoonfuls of dough onto a baking sheet., 8. Bake for 10-12 minutes or until edges are golden., 9. Allow to cool on a wire rack.'
    },
    {
        'name': 'Vegetable Stir-Fry',
        'description': 'Healthy stir-fry with a variety of colorful vegetables.',
        'image': '/images/vegetable_stir_fry.jpg',
        'ingredients': 'Broccoli, Bell peppers, Carrots, Snap peas, Soy sauce, Ginger, Garlic, Sesame oil',
        'instructions': '1. Cut vegetables into bite-sized pieces., 2. Heat sesame oil in a wok or skillet., 3. Add minced ginger and garlic., 4. Stir-fry vegetables until crisp-tender., 5. Add soy sauce for seasoning., 6. Serve hot.'
    },
    {
        'name': 'Homemade Tomato Soup',
        'description': 'Comforting tomato soup made from scratch.',
        'image': '/images/tomato_soup.jpg',
        'ingredients': 'Tomatoes, Onion, Garlic, Vegetable broth, Olive oil, Basil, Salt, Pepper',
        'instructions': '1. Saute chopped onion and garlic in olive oil., 2. Add chopped tomatoes and cook until soft., 3. Pour in vegetable broth and bring to a boil., 4. Simmer for 15-20 minutes., 5. Blend the soup until smooth., 6. Season with basil, salt, and pepper., 7. Serve hot.'
    },
    {
        'name': 'Grilled Salmon',
        'description': 'Healthy and flavorful grilled salmon fillets.',
        'image': '/images/grilled_salmon.jpg',
        'ingredients': 'Salmon fillets, Lemon, Olive oil, Dill, Salt, Pepper',
        'instructions': '1. Preheat grill to medium-high heat., 2. Brush salmon fillets with olive oil., 3. Squeeze lemon juice over the fillets., 4. Sprinkle with chopped dill, salt, and pepper., 5. Grill for 4-5 minutes per side or until cooked through., 6. Serve with lemon wedges.'
    },
    {
        'name': 'Vegetarian Tacos',
        'description': 'Delicious tacos filled with seasoned beans, veggies, and toppings.',
        'image': '/images/vegetarian_tacos.jpg',
        'ingredients': 'Black beans, Corn tortillas, Avocado, Tomato, Onion, Cilantro, Lime, Taco seasoning',
        'instructions': '1. Rinse and drain black beans., 2. Season beans with taco seasoning., 3. Warm corn tortillas., 4. Fill tortillas with seasoned beans., 5. Top with diced avocado, tomato, onion, and cilantro., 6. Squeeze lime over the tacos., 7. Enjoy!'
    },
    {
        'name': 'Mango Smoothie',
        'description': 'Refreshing smoothie with mango, yogurt, and banana.',
        'image': '/images/mango_smoothie.jpg',
        'ingredients': 'Mango, Yogurt, Banana, Honey, Ice cubes',
        'instructions': '1. Peel and dice mango., 2. Blend mango, yogurt, banana, honey, and ice cubes until smooth., 3. Pour into a glass and enjoy!'
    },
    {
        'name': 'Chicken Tikka Masala',
        'description': 'Rich and flavorful Indian chicken curry with a creamy tomato-based sauce.',
        'image': '/images/chicken_tikka_masala.jpg',
        'ingredients': 'Chicken thighs, Yogurt, Garam masala, Ginger, Garlic, Tomato puree, Heavy cream, Onion, Cilantro, Basmati rice',
        'instructions': '1. Marinate chicken in yogurt, garam masala, ginger, and garlic., 2. Grill or cook chicken until fully cooked., 3. In a pan, sauté chopped onion until golden., 4. Add tomato puree and cook until oil separates., 5. Stir in heavy cream and cooked chicken., 6. Simmer until the sauce thickens., 7. Garnish with chopped cilantro., 8. Serve over cooked basmati rice.'
    },
    {
        'name': 'Shrimp Scampi',
        'description': 'Garlicky shrimp served over pasta with a lemony butter sauce.',
        'image': '/images/shrimp_scampi.jpg',
        'ingredients': 'Shrimp, Linguine pasta, Butter, Olive oil, Garlic, Red pepper flakes, White wine, Lemon, Parsley, Salt, Pepper',
        'instructions': '1. Cook linguine pasta according to package instructions., 2. In a skillet, melt butter with olive oil., 3. Add minced garlic and red pepper flakes., 4. Sauté shrimp until pink and opaque., 5. Pour in white wine and squeeze lemon., 6. Season with salt and pepper., 7. Toss cooked pasta in the shrimp and sauce., 8. Garnish with chopped parsley.'
    },
    {
        'name': 'Vegetarian Pad Thai',
        'description': 'Thai stir-fried noodles with tofu, vegetables, and a tangy tamarind sauce.',
        'image': '/images/vegetarian_pad_thai.jpg',
        'ingredients': 'Rice noodles, Tofu, Bean sprouts, Carrots, Scallions, Peanuts, Eggs, Tamarind paste, Soy sauce, Lime, Sugar, Chili flakes',
        'instructions': '1. Soak rice noodles in hot water until softened., 2. In a wok, stir-fry tofu, carrots, and scallions., 3. Push ingredients to one side and scramble eggs., 4. Add soaked rice noodles to the wok., 5. In a small bowl, mix tamarind paste, soy sauce, lime juice, sugar, and chili flakes., 6. Pour sauce over the noodles and toss., 7. Garnish with bean sprouts and chopped peanuts.'
    },
    {
        'name': 'Quinoa Salad',
        'description': 'Nutritious salad with quinoa, mixed greens, veggies, and a zesty vinaigrette.',
        'image': '/images/quinoa_salad.jpg',
        'ingredients': 'Quinoa, Mixed greens, Cherry tomatoes, Cucumber, Avocado, Red onion, Feta cheese, Olive oil, Balsamic vinegar, Dijon mustard, Honey',
        'instructions': '1. Cook quinoa according to package instructions., 2. In a large bowl, combine cooked quinoa, mixed greens, halved cherry tomatoes, sliced cucumber, diced avocado, sliced red onion, and crumbled feta cheese., 3. In a small bowl, whisk together olive oil, balsamic vinegar, Dijon mustard, and honey to make the vinaigrette., 4. Drizzle the vinaigrette over the salad and toss to combine.'
    },
    {
        'name': 'Classic Caesar Salad',
        'description': 'Timeless Caesar salad with crisp romaine lettuce, croutons, and Caesar dressing.',
        'image': '/images/caesar_salad.jpg',
        'ingredients': 'Romaine lettuce, Croutons, Parmesan cheese, Caesar dressing',
        'instructions': '1. Wash and chop romaine lettuce., 2. Toss lettuce with croutons and shaved Parmesan cheese., 3. Drizzle Caesar dressing over the salad., 4. Toss until evenly coated., 5. Serve immediately.'
    },
    {
        'name': 'Mushroom Risotto',
        'description': 'Creamy Italian risotto with mushrooms and Parmesan cheese.',
        'image': '/images/mushroom_risotto.jpg',
        'ingredients': 'Arborio rice, Mushrooms, Onion, Garlic, White wine, Vegetable broth, Parmesan cheese, Butter, Olive oil',
        'instructions': '1. In a pan, sauté chopped onion and garlic in olive oil., 2. Add sliced mushrooms and cook until browned., 3. Stir in Arborio rice and cook until translucent., 4. Pour in white wine and cook until absorbed., 5. Gradually add vegetable broth, stirring continuously., 6. Continue adding broth until rice is creamy and cooked., 7. Stir in Parmesan cheese and butter., 8. Season with salt and pepper., 9. Serve hot.'
    },
    {
        'name': 'Lemon Herb Grilled Chicken',
        'description': 'Juicy grilled chicken marinated in a flavorful blend of lemon and herbs.',
        'image': '/images/lemon_herb_grilled_chicken.jpg',
        'ingredients': 'Chicken breasts, Lemon juice, Olive oil, Garlic, Fresh herbs (such as thyme and rosemary), Salt, Pepper',
        'instructions': '1. In a bowl, mix lemon juice, olive oil, minced garlic, chopped fresh herbs, salt, and pepper to create the marinade., 2. Coat chicken breasts with the marinade and let it sit for at least 30 minutes., 3. Preheat the grill., 4. Grill chicken until fully cooked, with beautiful grill marks., 5. Let it rest for a few minutes before serving.'
    },
    {
        'name': 'Homemade Guacamole',
        'description': 'Fresh and flavorful guacamole made with ripe avocados, tomatoes, onions, and lime.',
        'image': '/images/guacamole.jpg',
        'ingredients': 'Ripe avocados, Tomatoes, Red onion, Lime, Garlic, Jalapeño, Cilantro, Salt',
        'instructions': '1. Cut avocados in half, remove the pit, and scoop the flesh into a bowl., 2. Mash the avocados with a fork., 3. Dice tomatoes, finely chop red onion, mince garlic, and finely chop jalapeño. Add them to the bowl., 4. Squeeze lime juice over the mixture., 5. Stir in chopped cilantro and season with salt to taste'
    }
]

for recipe_data in recipes:
    Recipe.objects.create(**recipe_data).save()
    
    