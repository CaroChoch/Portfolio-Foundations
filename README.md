# <p align="center">Portfolio-Foundations</p>
<img width="100%" src="https://github.com/CaroChoch/Portfolio-Foundations/assets/113856302/d038e7cc-3fd4-4a76-9d0f-58f00c369c58">  
  
This project is a result of the collaborative efforts of [Mathieu Morel](https://github.com/MathieuMorel62) and [Caroline Chochoy](https://github.com/CaroChoch) as a part of their end-of-first-year portfolio project at [Holberton School](https://www.holbertonschool.fr/campus/lille), Lille. It was executed over a period of four weeks, highlighting the dedication and technical prowess of the team.

## 1. Introduction

Our application, Dream Shop, developed with the Django framework, provides a comprehensive platform for creating and managing an online store, as well as selling products. Our online store features a list of product categories, detailed information about each item, and a search function to facilitate navigation.
  
Designed with user-friendliness for consumers and ease of management for store administrators in mind, our application allows users to browse products, add them to their cart, and place orders with ease. Please note that our payment system has not been integrated yet, but we are actively working on implementing it in the near future.
  
Additionally, our application offers users the ability to create a personal account and easily log in. This will enable them to enjoy a personalized experience, keep track of their past orders, and securely manage their personal information.

## 2. Languages and technologies used

The development of our application was mainly based on the following languages and technologies:

- <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="25" height="25"/> **Python**: Main programming language used for backend development.
- <img src="https://www.svgrepo.com/show/373554/django.svg" width="25" height="25"> **Django**: Python-based web development framework.
- <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" width="25" height="25"> **HTML5**: Markup language used to structure and give meaning to web content.
- <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg" width="25" height="25">  **CSS3**: Style sheet language used to describe the appearance and formatting of the HTML document.
- <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" width="25" height="25"> **JavaScript**: Programming language used to make web pages interactive.
-  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg" width="25" height="25"> **MySQL**: Relational database management system used to store and retrieve data from our application.

All our templates were created without the help of CSS frameworks like Bootstrap, guaranteeing a unique and personalized appearance for our application.

## 3. Architecture and Operation
<p align="center">
<img src="https://github.com/CaroChoch/Portfolio-Foundations/assets/113856302/000e894a-a9f8-4e0e-8cc1-43ac4fc28247" width="100%" height="600">
</p>

- 👤 **User**: The user interacts with the user interface by sending requests (such as viewing a product, adding an item to the cart...) and receiving responses (such as viewing product details, confirming the addition of an item to the cart...).
   
- 🖥️ **User Interface (Frontend/UI)**: The user interface, built with HTML, CSS and JavaScript, sends user requests to the backend and displays responses from the backend to the user.  
    
- ⚙️ **Backend (Application Server)**: The backend, built with Django and Python, receives requests from the user interface. If a request requires interaction with the database (such as retrieving product details), the backend sends a request to the database and processes the response. The backend then sends the response to the user interface.
      
- 🗄️ **Database**: The MySQL database is used to store, retrieve, update and delete data based on requests received from the backend. Responses to backend requests are then returned to the backend.

## 4. Features
The application has several attractive features that improve the user experience and facilitate management tasks:

- `Store View`: Allows users to browse all available products. Products can be filtered according to their categories for a more targeted browsing experience.
- `Product Details View`: Offers detailed information about a specific product, including its name, description, price, availability, images, size and color variations.
- `Product Variations`: Effectively Manages product variations such as size and color, allowing each product to have several variations.
- `Search`: Allows users to search for products using keywords, displaying the results in a convenient way on the store page.
- `Cart Management`: Provides users with the opportunity to add products to their cart, view items in the cart and proceed with payment.
- `Registration`: Offers users the opportunity to create a personal account. This allows them to benefit from a personalized experience.
- `Login`: Allows registered users to easily log in to their account  
    
<img width="33%" alt="Capture d’écran 2023-06-27 à 16 49 01" src="https://github.com/CaroChoch/Portfolio-Foundations/assets/113856302/46950f24-bea2-4267-b347-9c1e6b91aa82"> <img width="33%" alt="Capture d’écran 2023-06-27 à 16 49 38" src="https://github.com/CaroChoch/Portfolio-Foundations/assets/113856302/68a62dc9-cba9-457d-92ff-7b4aad62853b"> <img width="33%" alt="Capture d’écran 2023-06-27 à 16 50 33" src="https://github.com/CaroChoch/Portfolio-Foundations/assets/113856302/566725a2-ebab-493e-95db-6c13348aa3ff">

## 5. Tests

The application has a complete suite of unit tests covering each section. We have set up tests for user accounts, registration forms, account views, baskets, cart items and products. We use the Python unittest library for our tests. We continue to add new tests and will add them for each feature we develop to maintain a high level of reliability and performance.
  
This rigorous testing approach allows us to detect and solve potential problems before they occur in a production environment. We are committed to providing a robust and reliable application, and testing plays an essential role in this goal.

<img width="1708" alt="Capture d’écran 2023-06-27 à 17 48 00" src="https://github.com/CaroChoch/Portfolio-Foundations/assets/113856302/f175621a-f3bf-41cd-8b09-fd30d9522c99">

## 6. Next steps / Features to come

Our vision for Dream Shop does not stop there. We are actively planning and developing new features to further improve the user experience and site management. Here are some of the improvements we are considering:
  
- 💳 **Payment System**: We are in the process of research and development to integrate a secure payment system into our application. This will allow users to place their orders directly from the platform, making the purchase process even simpler and more efficient.
  
- 📜 **Improved User History**: We plan to enrich the features of the user account by adding a detailed purchase history. Users will be able to review their past purchases, repeat a previous order, and much more.
  
- 🛡️ **Improved Security**: The security of our application and the protection of our users' data are our top priorities. We therefore plan to add additional layers of security to ensure the peace of mind of our users throughout their shopping experience.
  
We look forward to sharing these updates with you in the near future. Stay tuned for more information on the latest improvements to Dream Shop!

## 7. About

We like to collaborate and learn new things. Do not hesitate to contact us if you have any questions or comments about our work!

- Mathieu MOREL [<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30" height="30">](https://github.com/MathieuMorel62)  [<img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="30" height="30">](https://www.linkedin.com/in/mathieu-morel-9ab457261/)

- Caroline CHOCHOY [<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="30" height="30">](https://github.com/CaroChoch)  [<img src="https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" width="30" height="30">](https://www.linkedin.com/in/caroline-chochoy-11922a261/)
