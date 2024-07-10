# ShareBlast

![ShareBlast Logo](https://files.catbox.moe/fcj982.png)) <!-- Make sure to replace with the actual path to your screenshot -->

## Introduction

ShareBlast is a web application designed to streamline the process of collecting leads (emails and phone numbers) from social media giveaways. Our project is aimed at social media influencers, marketers, and businesses who run giveaways and need an efficient way to manage and collect participant information.

- **Deployed Site static**: [[ShareBlast](https://simowardi.github.io/shareblast.github.io/)]
- **Blog Article**: [[Read our project blog post](https://www.linkedin.com/pulse/shareblast-create-exciting-giveaways-minutes-mohamed-wardi-ir9we/?trackingId=fmX37TcsR9m6%2FMOvtfVvIQ%3D%3D)]
- **Authors**: 
  - [[MOHAMED WARDI](https://www.linkedin.com/in/mohamed-wardi-22874626a/)]


## Installation

To get started with ShareBlast, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/shareblast.git
    cd shareblast
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. **Run the application**:
    ```bash
    flask run
    ```

## Usage

1. **Register**: Create a new account by providing a username, email, and password.
2. **Login**: Log in with your registered credentials.
3. **Create Giveaway**: Set up a new giveaway and share the link with your audience.
4. **Collect Leads**: View and manage the collected leads from your giveaway.

## Contributing

We welcome contributions from the community! To contribute:

1. **Fork the repository**:
    ```bash
    git fork https://github.com/your-username/shareblast.git
    ```

2. **Create a new branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```

3. **Commit your changes**:
    ```bash
    git commit -m "Add your commit message here"
    ```

4. **Push to the branch**:
    ```bash
    git push origin feature/your-feature-name
    ```

5. **Create a pull request**: Go to the repository on GitHub and create a pull request.


## Licensing

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Advanced Details and Story

### Inspiration and Background

ShareBlast was inspired by the need for a more efficient way to collect and manage leads from social media giveaways. Our team, consisting of myself, Jane Doe, and John Smith, aimed to create a user-friendly platform that simplifies this process. Personally, I was motivated by my own experiences participating in various giveaways and noticing the inefficiencies in lead collection.

### Technical Challenges

One of the major challenges we faced was setting up Flask and Jinja2 templates to work seamlessly together. We encountered several bugs related to template rendering and form submission, which required us to dive deep into Flask's documentation and community forums for solutions.

Another significant challenge was working alone on certain aspects of the project, such as the core algorithms for lead management and the integration of SQLAlchemy for database interactions. This experience taught me the importance of meticulous planning and documentation to ensure smooth progress and debugging.

### Architecture

![Architecture Diagram](https://files.catbox.moe/gqgbey.png) <!-- Make sure to replace with the actual path to your architecture diagram -->

Our application follows a traditional MVC (Model-View-Controller) pattern. Here's a brief overview of the technologies used:

- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (for development), PostgreSQL (for production)

### Features

1. **User Authentication**: Users can register, log in, and log out securely.
2. **Giveaway Creation**: Users can create and manage their giveaways.
3. **Lead Collection**: Efficiently collect and view leads from giveaways.

### Most Difficult Technical Challenge

The most difficult technical challenge I encountered was integrating user authentication with Flask-Login. Initially, I faced issues with user sessions and ensuring that authenticated users were properly redirected. After extensive debugging and consultation with peers, we successfully implemented a robust authentication system.

### Lessons Learned

Through this project, I learned the importance of perseverance and the value of Time managment also effective problem solving trough itteration .
Additionally, I gained a deeper understanding of web development principles and the intricacies of Flask and SQLAlchemy.

## About Me

I am a passionate software engineer with a keen interest in web development, game development and digital marketing . This project has been an incredible learning experience, and I am excited to continue building and improving upon ShareBlast. 

- **GitHub**: https://github.com/simowardi/ShareBlast
- **Deployed Project**: https://github.com/simowardi/ShareBlast
- **LinkedIn**: https://www.linkedin.com/in/mohamed-wardi-22874626a/
