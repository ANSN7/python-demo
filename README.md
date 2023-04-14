# Enterprise Web Development - Assignment 1.

__Name:__ Alka Nixon

## Overview.

+ Upcoming movies page.
+ Top rated movies page.
+ Popular movies page.
+ Page for movies that are now playing in theatres.
+ Main actors list in movie details page.
+ List view for full cast and crew page (with new parameterized route).
+ Fantasy movie page where users can add and view their own movies.
+ Login and register page.
+ Supabase authentication - private and public routes.
+ Actor bio page, with personal details, social media profile links and profile images.
+ Pagination support for different category movies (All movies, Top rated, popular, now playing and upcoming).
+ Movie sorting functionality based on 8 parameters.
+ Sorting functionality in favourite movies page.
+ Extensive hyperlinking in actors and movies page.
+ Navigation on clicking logo.
+ New toolbar for different movie categories.
+ Must watch icon for upcoming movies.
+ Favourites icon in Movie details page if movie selected as favourite.
+ Updated title and logo to match the application scenario.
+ Responsive scroll bar for the image list in the movie and actor details page.






## Feature Design.

[ For each feature listed in the overview, show a screenshot(s) of its UI layout (use appropriate magnification for accessibility). Include captions with the images.]

e.g. 

#### The Upcoming Movies feature.

> Lists movies from the Upcoming movies endpoint of TMDB

![][image1]

#### Movies Reviews feature.

> Lists all the reviews for a particular movie (text extract only).

![][image2]

> Click the 'Full Review' link of an entry in the above list to show the full text of a review. 

![][image3]

.... other features .......

## Storybook.

[ Include a screenshot(s) from the Storybook UI and highlight the stories for new components developed.]

e.g.

![][image5]

## Authentication.

[ List all the routes in your app and highlight those that are protected/private (require authentication).]

e.g.

+ /movies - List of 20  movies from the Discover endpoint,
+ /movies/{movie_id} - Detailed information on a specific movie.
+ /reviews/{review_id} (Protected) - The full text of a movie review.
+ /movie/{movie_id}/similar - A list of similar movies. 
+ /person/{person_id} (Protected) - A specific actor's bio.
+ etc
+ etc

#### Protected features (if relevant)

[ Briefly state other areas where you used authentication in the app, for example, to protect access to functionality, e.g. only authenticated users can 'favourite' a movie.]

#### Supabase (if relevant)

[ Include a screenshot(s) from your Supabase account that verifies its use for this app. ]

## Deployment (if relevant).

[ Specify the URL of your deployed app and include a screenshot(s) from your deployment platform (e.g. Vercal) account that verifies its use for this app. Have a preregistered user for your app and specify their credentials.

Username: test1 ; Password: pass1
]

## Persistence (if relevant).

[ If you are persisting data to the Supabase backend, e.g. favourite movies, fantasy movie, include screenshots with appropriate captions to verify this aspect. ]

## Additional Information.

[ Briefly explain any other aspects of your app's design or implementation that is non-standard and worthy of mention.]

[image1]: ./images/img1.jpeg
[image2]: ./images/img2.jpeg
[image3]: ./images/img3.jpeg
[image4]: ./images/img4.jpeg
[image5]: ./images/img5.jpeg
