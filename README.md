# Overview:
Blog2CV is an innovative application that combines the power of blogging with resume creation to revolutionize the job application process. It provides users with a platform to effortlessly share their experiences, thoughts, and reflections through engaging blog posts. Additionally, users can draft a CV that summarizes their blog entries, providing recruiters with a comprehensive overview of their character, experiences, and skills.

# Key Features:
- **Blogging Platform:** Users can create and publish blog posts, expressing their thoughts, experiences, and expertise in various fields.
- **CV Creation:** The application allows users to generate a CV including their blog entries, highlighting their skills, achievements, and personal attributes.
- **User Profiles:** Each user has a profile where they can manage their blog posts, CVs, and other personal information.

# Installation:
To install Blog2CV, follow these steps:
1. Download and install `python 3.11.4`. Add the Python path to the System Env Variable and ensure the system finds it.
   ```
   https://www.python.org/downloads/release/python-3114
   ```
3. Clone the repository from GitHub.
   ```
   git clone https://github.com/Merina-tanjin/Capstone_project
   ```
4. Navigate to the project directory, create, and activate the environment
   ```
   cd Capstone_project
   py -m venv env
   .\env\Scripts\activate
   ```
7. Install the required dependencies using pip
   ```
   pip install -r requirements.txt
   ```
8. Run the application using Django's built-in development server
   ```
   cd django_project
   python manage.py run server
   ```
9. Access the application at the local server http://localhost:8000
10. To test the site you can use the below profile information or create a new one.
    ```
     Username: Merina
     Password: Shithi-49
      ```
# Dependencies:
- Python 3.11.4
- Django==5.0.2
- django-crispy-forms==2.1
- gensim==4.3.2
- nltk==3.8.1
- pandas==2.2.1
- scikit-learn==1.4.1.post1
- torch==2.2.2
- transformers==4.40.1

