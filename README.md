<h1>LDA-Based Unsupervised Document Topic Clustering</h1>

<h2>Project Overview</h2>
<p>This project uses Latent Dirichlet Allocation (LDA) to cluster over 90,000 CNN news articles into topics. It features a Flask backend API for real-time similarity search, allowing users to find the top-K most similar articles based on an input article. Redis is used for caching to improve search speed. The project is dockerized for easy deployment.</p>

<h2>Tech Stack</h2>
<ul>
    <li><strong>Python - Flask</strong> - Backend web framework</li>
    <li><strong>Gensim, spaCy</strong> - Topic modeling with LDA</li>
    <li><strong>Redis</strong> - Caching for faster similarity search</li>
    <li><strong>Docker</strong> - Containerization for deployment</li>
</ul>

<h2>Key Features</h2>
<ul>
    <li><strong>LDA Topic Clustering</strong>: Clusters documents into topics using Gensim's LDA.</li>
    <li><strong>Similarity Search</strong>: Real-time search for top-K most similar articles based on LDA topics.</li>
    <li><strong>Caching</strong>: Redis caching for fast search results.</li>
</ul>

<h2>How to Run</h2>
<ol>
    <li>Clone the repository.</li>
    <li>Navigate to the project directory.</li>
    <li>Run the project using Docker:
        <pre><code>docker-compose up --build</code></pre>
    </li>
</ol>

<h2>API Endpoint</h2>
<ul>
    <li><strong>POST /api/similarity_search</strong>: 
        <ul>
            <li>Input: Article text.</li>
            <li>Output: Top-K most similar articles.</li>
        </ul>
    </li>
</ul>

    <h2>Installation</h2>
    <p>To run without Docker:</p>
    <pre><code>pip install -r requirements.txt
flask run</code></pre>
    <p>Access the API at <strong>http://127.0.0.1:5000</strong>.</p>
