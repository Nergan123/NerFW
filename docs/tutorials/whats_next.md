# What's Next?

Now that you have created your game, you may need to host the application.
You can use the following services to host your game:
1. [Railway](https://railway.app/)
2. [Netlify](https://www.netlify.com/)
3. [AWS](https://aws.amazon.com/)
4. [Azure](https://azure.microsoft.com/)
5. [Vercel](https://vercel.com/)

**Important**: Do not use Heroku for your app. Heroku restarts the server every 24 hours.
NerFW uses SQLite as the database, basically it creates a file in the server and uses it as a database.
When the server restarts, the file is deleted and the database is lost.

## Containers

Some of the services mentioned above use containers
to host the application. You can copy the following content to a file named `Dockerfile`
in the root of your project to create a container for your application.

```Dockerfile
LABEL authors="nergan"

WORKDIR /app
COPY . .

WORKDIR /app
RUN pip install nerfw

EXPOSE 5000

CMD ["python", "main.py"]
```

This `Dockerfile` will create a container with your application and run it.
To create the container, you can use the following command:

```bash
docker build -t my-nerfw-app .
```

To run the container, you can use the following command:

```bash
docker run -p 5000:5000 my-nerfw-app
```

## Conclusion

You have created a game using NerFW. You have also learned how to host the application using containers.
You can now share your game with your friends.

Have fun!
