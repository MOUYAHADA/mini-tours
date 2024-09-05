```markdown
# Mini Tours

Mini Tours is a web application designed to help users explore and book various tours. This project serves as a portfolio MVP for the ALX program, showcasing skills in web development using Flask, HTML, CSS, and JavaScript.

## Features

- **Browse Tours**: Users can view a list of available tours with details such as name, description, and price.
- **Search Functionality**: Users can search for tours by name or description.
- **Tour Details**: Each tour has a dedicated page with detailed information and booking options.
- **Destinations**: Users can explore tours based on different destinations.
- **Contact Us**: Users can submit inquiries or messages through a contact form.
- **Booking System**: Users can book tours directly through the application.
- **Pagination**: Navigate through a large list of tours with pagination.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **HTML/CSS/TailwindCSS**: For the front-end user interface.
- **JavaScript & JQuery**: For dynamic content and form submissions.
- **JSON**: For storing tour data, descriptions, and destinations.
- **Jinja2**: Templating engine for rendering HTML pages.

## Installation

To set up the Mini Tours project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MOUYAHADA/mini-tours.git
   cd mini-tours
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Make sure you have Flask installed. You can install it using pip:
   ```bash
   pip install Flask
   ```

4. **Set Up Data Files**:
   Ensure that the `data` directory contains the following JSON files:
   - `tours.json`: Contains the list of tours.
   - `descriptions.json`: Contains descriptions for each tour.
   - `destinations.json`: Contains a list of destinations.

5. **Run the Application**:
   ```bash
   python app.py
   ```
   The application will be available at `http://127.0.0.1:5000`.

## Usage

- Navigate to the home page to view featured tours.
- Use the search bar to find specific tours by name or description.
- Click on a tour to view more details and book it.
- Explore different destinations to find related tours.
- Use the "Contact Us" form to send inquiries.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Flask community for their support and resources.
- Inspiration from various tour booking applications.