# cli

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Auth
JWT authentication has now been setup. In order to protect an endpoint in the router, add the following:
``` js
// Standard endpoint - no login required
{
    path: "/activitycenter",
    name: "Activity",
    component: ActivityCenter,
},

// Endpoint with login required
{
    path: "/activitycenter",
    name: "Activity",
    component: ActivityCenter,
    meta: { requiresAuth: true} // Just need to add this line
},
```

For any API requests that also require authentication (basically any API requests made from inside a page requiring login to access), you need to use `axiosAuth` instead of `axios`.
Do this as shown:
```js
// Witouth axiosAuth
const response = await axios.get(
    `http://localhost:5001/test`
);

// With axiosAuth
import axiosAuth from "@/api/axios-auth"    // This can go at the top of the file
const response = await axiosAuth.get(
    `/test`
);
```
