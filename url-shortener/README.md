# 🔗 URL Shortener with Authentication

A full-stack **URL Shortener Application** built with **Node.js**, **Express.js**, **MongoDB**, and **EJS**, featuring secure **cookie-based user authentication and authorization**. Users can register, log in, generate compact 8-character unique short links, view their personalized dashboard with URL history, and track real-time click analytics.

---

## 🚀 Features

- 🔐 **User Authentication & Authorization**: Complete Sign Up and Login flow with cookie-based session management (`uuid` & `cookie-parser`).
- 👤 **Personalized User Dashboard**: Authenticated users can view and manage only the URLs they have created.
- ✂️ **Unique Short URL Generation**: Generates 8-character unique short IDs using `nanoid`.
- 🔁 **Duplicate Detection**: Prevents duplicate entries if a user has already shortened the target URL.
- 📊 **Visit Analytics & Tracking**: Tracks total clicks and logs timestamps for every redirection.
- ⚡ **Fast Redirection**: Instant 302 redirection to the target destination.
- 🛡️ **Protected Routes & Middlewares**:
  - `restrictToLoggedinUseOnly`: Restricts shortening and dashboard access to authenticated users.
  - `checkAuth`: Inlines user context for static pages.
- 🎨 **Server-Side Rendered UI**: Interactive web interface rendered using **EJS** (Home, Login, and Sign Up views).

---

## 🛠️ Tech Stack

- **Runtime Environment:** [Node.js](https://nodejs.org/)
- **Web Framework:** [Express.js](https://expressjs.com/) (v5)
- **Database & ODM:** [MongoDB](https://www.mongodb.com/) with [Mongoose](https://mongoosejs.com/)
- **Template Engine:** [EJS](https://ejs.co/)
- **Session & Auth Management:** `uuid` & `cookie-parser`
- **ID Generator:** [NanoID](https://github.com/ai/nanoid)
- **Dev Tooling:** [Nodemon](https://nodemon.io/)

---

## 📁 Project Structure

```text
url-shortener/
├── controllers/
│   ├── url.js            # Controller for generating short URLs, redirection, & analytics
│   └── user.js           # Controller for user signup and login
├── middlewares/
│   └── auth.js           # Route protection & authentication middleware
├── models/
│   ├── url.js            # Mongoose schema for URLs (shortId, redirectURL, visitHistory, createdBy)
│   └── user.js           # Mongoose schema for Users (name, email, password)
├── routes/
│   ├── staticRouter.js   # Routes for rendering UI pages (Home, Login, Sign Up)
│   ├── url.js            # Routes for URL operations (POST /url, GET /url/:shortId, GET /url/analytics/:shortId)
│   └── user.js           # Routes for user actions (POST /user/signup, POST /user/login)
├── service/
│   └── auth.js           # In-memory session store mapping session IDs to users
├── views/
│   ├── home.ejs          # Main dashboard view with URL creation form and table
│   ├── login.ejs         # User login view
│   └── signup.ejs        # User registration view
├── connection.js         # MongoDB connection module
├── index.js              # Application entry point & Express server setup
├── package.json          # Project dependencies and npm scripts
└── README.md             # Project documentation
```

---

## 🔐 Authentication & Session Flow

1. **Sign Up (`POST /user/signup`)**:
   - Saves new user credentials (`name`, `email`, `password`) in MongoDB.
   - Redirects to `/`.

2. **Login (`POST /user/login`)**:
   - Validates user credentials against MongoDB.
   - Generates a unique UUID `sessionId`.
   - Stores `sessionId -> user` mapping in the server's session store (`service/auth.js`).
   - Sets a `uid` cookie in the user's browser and redirects to the home dashboard.

3. **Route Protection (`middlewares/auth.js`)**:
   - `restrictToLoggedinUseOnly`: Reads `req.cookies.uid`, resolves user from session store. If missing or invalid, redirects to `/login`.
   - `checkAuth`: Checks for `req.cookies.uid` and populates `req.user` without forcing a redirect.

---

## 📡 API & Route Reference

### 1. View & Navigation Routes

| Method | Route | Access | Description |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | Protected | Renders Home dashboard with user's shortened URLs |
| **GET** | `/login` | Public | Renders the Login page |
| **GET** | `/signup` | Public | Renders the Sign Up page |

### 2. User Authentication Routes

| Method | Route | Description | Action |
| :--- | :--- | :--- | :--- |
| **POST** | `/user/signup` | Registers a new user account | Redirects to `/` |
| **POST** | `/user/login` | Authenticates user & sets session cookie `uid` | Redirects to `/` |

### 3. URL Operations & Analytics Routes

| Method | Endpoint | Access | Description | Response |
| :--- | :--- | :--- | :--- | :--- |
| **POST** | `/url` | Protected | Creates a new short URL linked to the logged-in user | HTML / EJS |
| **GET** | `/url/:shortId` | Public | Redirects to original URL and records click timestamp | 302 Redirect |
| **GET** | `/url/analytics/:shortId` | Public | Returns total click count and timestamp history | JSON |

#### Example Analytics JSON Response (`GET /url/analytics/:shortId`)

```json
{
  "totalClicks": 3,
  "analytics": [
    { "timestamp": 1727622800000 },
    { "timestamp": 1727622850000 },
    { "timestamp": 1727622910000 }
  ]
}
```

---

## 📝 Database Schemas

### User Schema (`models/user.js`)

```javascript
const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
    unique: true,
  },
  password: {
    type: String,
    required: true,
  }
}, { timestamps: true });
```

### URL Schema (`models/url.js`)

```javascript
const urlSchema = new mongoose.Schema({
  shortId: {
    type: String,
    required: true,
    unique: true,
  },
  redirectURL: {
    type: String,
    required: true,
  },
  visitHistory: [
    {
      timestamp: { type: Number }
    }
  ],
  createdBy: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "users"
  }
}, { timestamps: true });
```

---

## ⚙️ Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v16.x or higher)
- [MongoDB](https://www.mongodb.com/try/download/community) installed and running locally on `mongodb://127.0.0.1:27017`

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MoreVishwajeet/url-shortener-flask.git
   cd url-shortener
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start MongoDB:**
   Ensure MongoDB service is running:
   ```bash
   mongod
   ```

4. **Start the application:**
   ```bash
   npm start
   ```

5. **Open in Browser:**
   Navigate to:
   ```text
   http://localhost:8001
   ```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or create a pull request.

---

## 📄 License

This project is licensed under the [ISC License](package.json).
