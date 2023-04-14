# How to secure an API REST for mobile app? (if sniffing requests gives you the "key")
It's probable a newbie question but I'll try to create an interesting debate.

I know there are some authentication methods for API Basic Authentication, API Keys, OAuth 2.0 ... all of those methods add a header or a formData param in the request.

Although you use SSL, it's "usually easy" to hack mobile apps (I'm thinking in Android right now: decompiling the app, changing manifest to allow custom SSL, compiling again and sniffing through a SSL proxy all the requests).

In those requests I've found a lot of auth keys that I can use in other calls from a console, simulating the app with no problems.

So, now I've hacked some APIs in mobile apps, my question is: is there any way to secure an API in a mobile app?

I wonder if one securitization layer would be to limit the number of requests per "key".

Am I wrong? Am I missing something? Is this a stupid question?
