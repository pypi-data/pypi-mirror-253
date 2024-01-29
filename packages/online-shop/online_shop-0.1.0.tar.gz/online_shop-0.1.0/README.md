## Deployment

Add additional notes about how to deploy this on a live system.

## Built With

- Django
- Django Rest Framework
- Django Channels
- Docker

## Preparation

Follow these steps to set up the project:

1. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

2. Activate the virtual environment:

   ```sh
   .\venv\Scripts\activate.bat
   ```

3. Run docker

   ```sh
   docker-compose up -d
   ```

4. Install online shop:

   ```sh
   py -m build
   ```
 
5. Install online shop:

   ```sh
   python -m online_shop.manage runserver
   ```


## Tests

   ```sh
   cd online_shop
   ```

   ```sh
   pip install -r requirements/requirements.txt
   ```

   ```sh
   python manage.py test
   ```

## Authors

Paweł Kwieciński