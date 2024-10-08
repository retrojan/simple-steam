/* Общий стиль для сайта */
body {
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #1e1e1e;
    color: #e1e1e1;
}

.header {
    text-align: center;
    padding: 50px 20px;
    background-color: #252526;
    border-bottom: 1px solid #3c3c3c;
}

.header h1 {
    font-size: 48px;
    margin: 0;
    color: #ffffff;
}

.header p {
    font-size: 20px;
    margin-top: 10px;
    color: #a1a1a1;
}

.content {
    display: flex;
    justify-content: center;
    align-items: center;
    height: calc(100vh - 200px);
}

.download-section {
    text-align: center;
}

.download-section h2 {
    font-size: 32px;
    color: #ffffff;
    margin-bottom: 20px;
}

.download-button {
    font-size: 18px;
    text-decoration: none;
    padding: 15px 30px;
    background-color: #ffffff;
    color: #252526;
    border-radius: 8px;
    transition: background 0.5s ease-in-out, color 0.5s ease-in-out;
    font-weight: bold;
}

.download-button:hover {
    background: linear-gradient(90deg, #ff007a, #ffffff);
    color: #ff007a;
}

/* Footer */
.footer {
    text-align: center;
    padding: 20px;
    background-color: #252526;
    border-top: 1px solid #3c3c3c;
    color: #a1a1a1;
}
