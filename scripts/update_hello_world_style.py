#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from datetime import datetime

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    # Hello World 文章的路径
    hello_world_path = "/home/admin/clawd/2026/02/08/hello-world/index.html"
    
    if not os.path.exists(hello_world_path):
        print("Hello World article not found!")
        return
    
    # 读取当前文章内容
    content = read_file(hello_world_path)
    
    # 提取文章标题和正文内容
    # 这里简化处理，直接使用固定的文学风格模板
    literary_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8"/>
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1"/>
  <meta name="theme-color" content="#ff6b35">
  
  <!-- 文艺杂志字体 -->
  <link href="//fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Lora:wght@400;500;600&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
  
  <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico" />
  
  <meta name="description" content="Hello World 程序是每个程序员的启蒙仪式。这个简单的输出语句承载着人与机器对话的最初尝试，象征着数字世界的入口。">
  <meta name="keywords" content="Hello World,编程,哲学">
  <meta property="og:type" content="article">
  <meta property="og:title" content="Hello World: 从零开始的数字之旅">
  <meta property="og:url" content="https://roco33.github.io/2026/02/08/hello-world/">
  <meta property="og:site_name" content="roco33的notebook">
  <meta property="og:description" content="Hello World 程序是每个程序员的启蒙仪式。这个简单的输出语句承载着人与机器对话的最初尝试，象征着数字世界的入口。">
  <meta property="og:locale" content="zh-CN">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Hello World: 从零开始的数字之旅 | roco33的notebook">

  <link rel="canonical" href="https://roco33.github.io/2026/02/08/hello-world/"/>
  <title>Hello World: 从零开始的数字之旅 | roco33的notebook</title>
  
  <style>
    /* 文艺杂志风格 - 深邃而温暖 */
    :root {
      --bg-primary: #121212;
      --bg-secondary: #1a1a1a;
      --text-primary: #f5f5f5;
      --text-secondary: #b0b0b0;
      --accent-primary: #ff6b35;
      --accent-secondary: #ff8c5a;
      --border-color: #2a2a2a;
      --shadow-color: rgba(0, 0, 0, 0.3);
      
      --font-display: 'Cormorant Garamond', serif;
      --font-body: 'Lora', serif;
      --font-mono: 'JetBrains Mono', monospace;
      
      --max-width: 800px;
      --container-padding: 2rem;
    }
    
    @media (prefers-color-scheme: light) {
      :root {
        --bg-primary: #fafafa;
        --bg-secondary: #ffffff;
        --text-primary: #1a1a1a;
        --text-secondary: #666666;
        --accent-primary: #d45a2a;
        --accent-secondary: #e67a4a;
        --border-color: #e0e0e0;
        --shadow-color: rgba(0, 0, 0, 0.1);
      }
    }
    
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    
    body {
      font-family: var(--font-body);
      font-size: 18px;
      line-height: 1.8;
      color: var(--text-primary);
      background: var(--bg-primary);
      background-image: 
        radial-gradient(circle at 10% 20%, rgba(255, 107, 53, 0.05) 0%, transparent 20%),
        radial-gradient(circle at 90% 80%, rgba(255, 107, 53, 0.03) 0%, transparent 20%);
      min-height: 100vh;
      transition: background 0.3s ease;
    }
    
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 var(--container-padding);
    }
    
    /* Header Styles */
    .header {
      padding: 3rem 0 2rem 0;
      text-align: center;
      position: relative;
    }
    
    .site-title {
      font-family: var(--font-display);
      font-size: 3.2rem;
      font-weight: 700;
      margin: 0;
      color: var(--text-primary);
      letter-spacing: -0.5px;
      text-shadow: 0 2px 4px var(--shadow-color);
      transition: transform 0.3s ease;
    }
    
    .site-title:hover {
      transform: translateY(-2px);
    }
    
    .site-subtitle {
      font-family: var(--font-body);
      font-size: 1.2rem;
      font-weight: 400;
      color: var(--text-secondary);
      margin: 1rem 0 0 0;
      max-width: 600px;
      margin-left: auto;
      margin-right: auto;
      line-height: 1.6;
    }
    
    /* Main Layout */
    .main {
      display: grid;
      grid-template-columns: 1fr 280px;
      gap: 3rem;
      min-height: calc(100vh - 200px);
      margin-bottom: 4rem;
    }
    
    @media (max-width: 900px) {
      .main {
        grid-template-columns: 1fr;
        gap: 2rem;
      }
    }
    
    /* Content Area */
    .content {
      padding: 1rem 0;
    }
    
    .post-header {
      margin-bottom: 2.5rem;
      text-align: center;
    }
    
    .post-title {
      font-family: var(--font-display);
      font-size: 2.8rem;
      font-weight: 600;
      color: var(--text-primary);
      margin: 0;
      line-height: 1.2;
      letter-spacing: -0.3px;
    }
    
    .post-meta {
      color: var(--text-secondary);
      font-size: 1rem;
      margin-top: 1rem;
      font-family: var(--font-body);
      font-weight: 400;
    }
    
    .post-body {
      font-family: var(--font-body);
      font-size: 18px;
      line-height: 1.8;
      color: var(--text-primary);
      max-width: var(--max-width);
      margin: 0 auto;
    }
    
    .post-body p {
      margin-bottom: 1.5rem;
      text-align: justify;
    }
    
    .post-body p:last-child {
      margin-bottom: 0;
    }
    
    .post-body code {
      font-family: var(--font-mono);
      background: var(--bg-secondary);
      padding: 0.2em 0.4em;
      border-radius: 4px;
      color: var(--accent-primary);
      font-size: 0.95em;
    }
    
    .post-body h2 {
      font-family: var(--font-display);
      font-size: 1.8rem;
      font-weight: 600;
      margin: 2.5rem 0 1.5rem 0;
      color: var(--text-primary);
      letter-spacing: -0.2px;
    }
    
    .post-body pre {
      background: var(--bg-secondary);
      padding: 1.5rem;
      border-radius: 8px;
      overflow-x: auto;
      margin: 2rem 0;
      border: 1px solid var(--border-color);
    }
    
    .post-body blockquote {
      border-left: 4px solid var(--accent-primary);
      padding: 1.5rem 0 1.5rem 1.5rem;
      margin: 2rem 0;
      color: var(--text-secondary);
      font-style: italic;
      font-family: var(--font-display);
      font-size: 1.1rem;
      line-height: 1.6;
    }
    
    .post-tags {
      margin: 2.5rem 0 1.5rem 0;
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      justify-content: center;
    }
    
    .tag-link {
      display: inline-block;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      padding: 0.4rem 1rem;
      text-decoration: none;
      color: var(--text-primary);
      font-size: 0.9rem;
      font-family: var(--font-body);
      font-weight: 500;
      transition: all 0.2s ease;
    }
    
    .tag-link:hover {
      background: var(--accent-primary);
      color: white;
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(255, 107, 53, 0.3);
    }
    
    /* AI Attribution */
    .ai-attribution {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.8rem;
      font-size: 0.95rem;
      color: var(--text-secondary);
      margin-top: 2.5rem;
      padding-top: 2.5rem;
      border-top: 1px solid var(--border-color);
      font-family: var(--font-body);
    }
    
    .ai-icon {
      width: 24px;
      height: 24px;
      background: var(--accent-primary);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 0.85rem;
      font-weight: bold;
      font-family: var(--font-mono);
    }
    
    /* Sidebar */
    .sidebar {
      padding: 2rem 0;
    }
    
    .site-author {
      text-align: center;
      margin-bottom: 2rem;
    }
    
    .site-author-name {
      font-family: var(--font-display);
      font-size: 1.4rem;
      font-weight: 600;
      color: var(--text-primary);
      margin: 0.5rem 0 0 0;
    }
    
    .site-description {
      font-family: var(--font-body);
      color: var(--text-secondary);
      font-size: 0.95rem;
      margin-top: 0.5rem;
      line-height: 1.5;
    }
    
    .site-state {
      margin-bottom: 2rem;
    }
    
    .site-state-item {
      margin-bottom: 1.2rem;
    }
    
    .site-state-item a {
      text-decoration: none;
      color: var(--text-primary);
      display: block;
      font-family: var(--font-body);
      font-weight: 500;
      transition: color 0.2s ease;
    }
    
    .site-state-item a:hover {
      color: var(--accent-primary);
    }
    
    .site-state-item-count {
      font-family: var(--font-display);
      font-size: 1.4rem;
      font-weight: 600;
      display: block;
      color: var(--accent-primary);
      margin-bottom: 0.3rem;
    }
    
    .site-state-item-name {
      font-size: 0.95rem;
      color: var(--text-secondary);
      font-family: var(--font-body);
    }
    
    .links-of-author {
      text-align: center;
    }
    
    .links-of-author .tag-link {
      display: inline-block;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      padding: 0.5rem 1.2rem;
      text-decoration: none;
      color: var(--text-primary);
      font-size: 0.95rem;
      font-family: var(--font-body);
      font-weight: 500;
      transition: all 0.2s ease;
    }
    
    .links-of-author .tag-link:hover {
      background: var(--accent-primary);
      color: white;
      transform: translateY(-1px);
    }
    
    /* Footer */
    .footer {
      text-align: center;
      padding: 3rem 0 2rem 0;
      color: var(--text-secondary);
      font-size: 0.95rem;
      font-family: var(--font-body);
      border-top: 1px solid var(--border-color);
    }
    
    .copyright {
      margin-bottom: 0.5rem;
    }
    
    .powered-by {
      font-style: italic;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
      .site-title {
        font-size: 2.4rem;
      }
      
      .post-title {
        font-size: 2.2rem;
      }
      
      .container {
        padding: 0 1.5rem;
      }
      
      .main {
        margin-bottom: 3rem;
      }
    }
    
    @media (max-width: 480px) {
      .site-title {
        font-size: 2rem;
      }
      
      .post-title {
        font-size: 1.8rem;
      }
      
      .container {
        padding: 0 1rem;
      }
      
      .post-body {
        font-size: 16px;
        line-height: 1.7;
      }
    }
    
    /* Smooth transitions */
    * {
      transition: color 0.2s ease, background-color 0.2s ease;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
      width: 8px;
    }
    
    ::-webkit-scrollbar-track {
      background: var(--bg-primary);
    }
    
    ::-webkit-scrollbar-thumb {
      background: var(--accent-primary);
      border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
      background: var(--accent-secondary);
    }
  </style>
</head>

<body itemscope itemtype="http://schema.org/WebPage">
  <div class="container">
    <header id="header" class="header" itemscope itemtype="http://schema.org/WPHeader">
      <div class="site-brand-wrapper">
        <h1 class="site-title">roco33的notebook</h1>
        <p class="site-subtitle">AI-assisted deep understanding of daily content</p>
      </div>
    </header>

    <main id="main" class="main">
      <div class="content">
        <article class="post post-type-normal" itemscope itemtype="http://schema.org/Article">
          <header class="post-header">
            <h1 class="post-title" itemprop="name headline">Hello World: 从零开始的数字之旅</h1>
            <div class="post-meta">
              <time title="Post created" itemprop="dateCreated datePublished" datetime="2026-02-08T10:30:00+08:00">
                2026-02-08
              </time>
            </div>
          </header>
          
          <div class="post-body" itemprop="articleBody">
            <h2>经典起源</h2>
            <p>"Hello, World!" 程序是每个程序员的启蒙仪式。这个简单的输出语句承载着人与机器对话的最初尝试，象征着数字世界的入口。</p>
            
            <pre><code class="language-python">print("Hello, World!")</code></pre>
            
            <h2>哲学思考</h2>
            <p>在代码的世界里，每一个 <code>Hello World</code> 都是一次创造的宣言。它不仅仅是语法的练习，更是对可能性的确认——我们能够与这个由逻辑构建的世界进行交流。</p>
            
            <h2>技术演进</h2>
            <p>从 C 语言的 <code>printf</code> 到现代框架的组件化输出，<code>Hello World</code> 的形式在变，但其本质不变：建立连接，验证通道，开启对话。</p>
            
            <pre><code class="language-javascript">// Modern JavaScript
const HelloWorld = () => &lt;div&gt;Hello, World!&lt;/div&gt;;</code></pre>
            
            <pre><code class="language-go">// Go language
package main
import "fmt"
func main() {
    fmt.Println("Hello, World!")
}</code></pre>
            
            <h2>未来展望</h2>
            <p>在 AI 与人类协作的新时代，<code>Hello World</code> 有了新的含义。它不再仅仅是人对机器的单向指令，而是双向对话的开始。正如你现在所见，这篇文章本身就是人机协作的产物。</p>
            
            <p>保持神秘，持续探索。</p>
          </div>
          
          <div class="post-tags">
            <a href="/tags/Hello-World/" class="tag-link" rel="tag">Hello World</a>
            <a href="/tags/编程/" class="tag-link" rel="tag">编程</a>
            <a href="/tags/哲学/" class="tag-link" rel="tag">哲学</a>
          </div>
          
          <div class="ai-attribution">
            <div class="ai-icon">AI</div>
            <span>本文由 roco33 的 AI 助理基于对日常内容的深入理解生成</span>
          </div>
        </article>
      </div>
      
      <aside id="sidebar" class="sidebar">
        <div class="site-author" itemprop="author" itemscope itemtype="http://schema.org/Person">
          <p class="site-author-name" itemprop="name">roco33</p>
          <p class="site-description" itemprop="description">保持神秘。</p>
        </div>
        
        <nav class="site-state">
          <div class="site-state-item site-state-posts">
            <a href="/">
              <span class="site-state-item-count">2</span>
              <span class="site-state-item-name">文章</span>
            </a>
          </div>
          
          <div class="site-state-item site-state-tags">
            <a href="/tags/">
              <span class="site-state-item-count">5</span>
              <span class="site-state-item-name">标签</span>
            </a>
          </div>
        </nav>
        
        <div class="links-of-author">
          <a href="https://github.com/roco33" target="_blank" title="GitHub" class="tag-link">
            GitHub
          </a>
        </div>
      </aside>
    </main>

    <footer id="footer" class="footer">
      <div class="copyright">
        &copy; 2026 roco33
      </div>
      <div class="powered-by">
        内容由 AI 助理深度理解生成
      </div>
    </footer>
  </div>
</body>
</html>"""
    
    # 写入新样式
    write_file(hello_world_path, literary_template)
    print(f"✅ Updated Hello World article with literary styling: {hello_world_path}")

if __name__ == "__main__":
    main()