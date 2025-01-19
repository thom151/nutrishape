# Nutrishape - Your Recipe Chatbot

## 📖 Description
**Nutrishape** is a Django-powered chatbot application that provides users with instant recipe suggestions. Users can interact with the chatbot, get clickable recipe links, and view detailed instructions for each recipe.

## 🤔 Why Nutrishape?

In today’s fast-paced world, finding quick, reliable, and healthy recipes can be challenging. Nutrishape simplifies this process by providing instant recipe recommendations tailored to user preferences. By integrating chatbot functionality, users can effortlessly ask for recipe suggestions and view detailed instructions, all within a single platform.


---

## 🧐 Overview

![Demo of Nutrishape chatbot](nutrishape.mp4)

## 🚀 Quick Start

Follow these steps to set up and run **Nutrishape** on your local machine.

### Prerequisites
Before starting, ensure you have:
1. [Python 3.x](https://www.python.org/) installed on your machine.
2. Django 4.x installed (handled in the installation steps).
3. SQLite (default database).

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/thom-151/nutrishape
   cd nutrishape
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Navigate to `nutrition/helpers.py` and replace the OpenAI API key with your own key on the specified line. 
   **Note**  you need to provide at least $1 for the API to work effectively.

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application in your browser:
   - Visit: `http://127.0.0.1:8000/`

---

## How to Use Nutrishape

1. **Home Page**
   - Navigate to the homepage to explore the features of Nutrishape.

2. **Login/Register**
   - Use the `Register` page to create an account.
   - Use the `Login` page to access your account.

3. **Chat with the Bot**
   - Go to the `Chat` section and start a conversation with the bot.
   - Ask for recipes by typing phrases like "Suggest a pasta recipe" or "Show me healthy recipes."

4. **View Full Recipe Details**
   - When the bot suggests a recipe, click on it to view the full details, such as ingredients and preparation steps.

---


## Technologies Used

- **Backend**: Django (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript

---

## Future Enhancements

- Add user preferences for more personalized recipe recommendations.
- Integrate a wider range of recipe sources.
- Provide nutritional information for each recipe.
- Implement advanced filtering options based on dietary restrictions.

---

## Contributions

Contributions are welcome! Feel free to submit a pull request or raise an issue for discussion.

## 🤝 Need Help?

If you encounter any issues or have questions:
- Open an issue in this repository.
- Contact me at [thomassantos2003@gmail.com](mailto:thomassantos2003@gmail.com)

---

Enjoy using **Nutrishape** to bring your favorite stories to life! 🎉
