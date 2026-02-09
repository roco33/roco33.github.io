#!/bin/bash

# Update homepage to include latest daily reflection post
echo "Updating homepage with latest posts..."

# Get current date
DATE=$(date +"%Y-%m-%d")
YEAR=$(date +"%Y")
MONTH=$(date +"%m")
DAY=$(date +"%d")

# Create temporary homepage
TEMP_INDEX="/home/admin/clawd/index.html.tmp"

# Backup current homepage
cp /home/admin/clawd/index.html /home/admin/clawd/index.html.bak

# Extract the header and style section (everything before the posts section)
HEADER_START='<section id="posts" class="posts-expand">'
HEADER_END='</section>'

# Get everything before the posts section
sed -n '1,/'"$HEADER_START"'/p' /home/admin/clawd/index.html | head -n -1 > "$TEMP_INDEX"

# Add the posts section start
echo '        <section id="posts" class="posts-expand">' >> "$TEMP_INDEX"

# Add the latest daily reflection post (if exists)
if [ -f "/home/admin/clawd/$YEAR/$MONTH/$DAY/daily-reflection/index.md" ]; then
    # Read the markdown file and extract title and content
    POST_CONTENT=$(cat "/home/admin/clawd/$YEAR/$MONTH/$DAY/daily-reflection/index.md")
    
    # Extract title (first line)
    TITLE=$(echo "$POST_CONTENT" | head -n 1 | sed 's/^# //')
    
    # Extract body (skip first line)
    BODY=$(echo "$POST_CONTENT" | tail -n +2)
    
    # Convert markdown paragraphs to HTML
    HTML_BODY=""
    while IFS= read -r line; do
        if [[ -n "$line" ]]; then
            HTML_BODY+="<p>$line</p>"
        fi
    done <<< "$BODY"
    
    # Add the post to homepage
    cat >> "$TEMP_INDEX" << EOF
          
          <!-- Daily Reflection Post -->
          <article class="post post-type-normal" itemscope itemtype="http://schema.org/Article">
            <div class="post-block glass-effect">
              <link itemprop="mainEntityOfPage" href="https://roco33.github.io/$YEAR/$MONTH/$DAY/daily-reflection/">
              
              <span hidden itemprop="author" itemscope itemtype="http://schema.org/Person">
                <meta itemprop="name" content="roco33">
                <meta itemprop="description" content="">
                <meta itemprop="image" content="/images/avatar.jpg">
              </span>
              
              <span hidden itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
                <meta itemprop="name" content="roco33的notebook">
              </span>
              
              <header class="post-header">
                <h1 class="post-title" itemprop="name headline">
                  <a class="post-title-link" href="/$YEAR/$MONTH/$DAY/daily-reflection/" itemprop="url">$TITLE</a>
                </h1>
                
                <div class="post-meta">
                  <span class="post-time">
                    <time title="Post created" itemprop="dateCreated datePublished" datetime="$DATE"T04:00:00+08:00">
                      $DATE
                    </time>
                  </span>
                </div>
              </header>
              
              <div class="post-body" itemprop="articleBody">
                $HTML_BODY
              </div>
              
              <div class="post-tags">
                <a href="/tags/哲学/" class="tag-link" rel="tag">哲学</a>
                <a href="/tags/认知/" class="tag-link" rel="tag">认知</a>
                <a href="/tags/知识/" class="tag-link" rel="tag">知识</a>
              </div>
              
              <div class="ai-attribution">
                <div class="ai-icon">AI</div>
                <span>本文由 roco33 的 AI 助理基于对日常内容的深入理解生成</span>
              </div>
            </div>
          </article>
EOF
fi

# Add existing Hello World post
cat >> "$TEMP_INDEX" << 'EOF'
          
          <!-- Hello World Post -->
          <article class="post post-type-normal" itemscope itemtype="http://schema.org/Article">
            <div class="post-block glass-effect">
              <link itemprop="mainEntityOfPage" href="https://roco33.github.io/2026/02/08/hello-world/">
              
              <span hidden itemprop="author" itemscope itemtype="http://schema.org/Person">
                <meta itemprop="name" content="roco33">
                <meta itemprop="description" content="">
                <meta itemprop="image" content="/images/avatar.jpg">
              </span>
              
              <span hidden itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
                <meta itemprop="name" content="roco33的notebook">
              </span>
              
              <header class="post-header">
                <h1 class="post-title" itemprop="name headline">
                  <a class="post-title-link" href="/2026/02/08/hello-world/" itemprop="url">Hello World: 从零开始的数字之旅</a>
                </h1>
                
                <div class="post-meta">
                  <span class="post-time">
                    <time title="Post created" itemprop="dateCreated datePublished" datetime="2026-02-08T10:30:00+08:00">
                      2026-02-08
                    </time>
                  </span>
                </div>
              </header>
              
              <div class="post-body" itemprop="articleBody">
                <p>"Hello, World!" 程序是每个程序员的启蒙仪式。这个简单的输出语句承载着人与机器对话的最初尝试，象征着数字世界的入口。</p>
                <p>在代码的世界里，每一个 <code>Hello World</code> 都是一次创造的宣言。它不仅仅是语法的练习，更是对可能性的确认——我们能够与这个由逻辑构建的世界进行交流。</p>
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
            </div>
          </article>
EOF

# Add the closing section
cat >> "$TEMP_INDEX" << 'EOF'
          
        </section>
      </div>
      
      <aside id="sidebar" class="sidebar glass-effect">
        <div class="site-author" itemprop="author" itemscope itemtype="http://schema.org/Person">
          <img class="site-author-image" itemprop="image" src="/images/avatar.jpg" alt="roco33" />
          <p class="site-author-name" itemprop="name">roco33</p>
          <p class="site-description" itemprop="description">保持神秘。</p>
        </div>
        
        <nav class="site-state">
          <div class="site-state-item site-state-posts">
            <a href="/">
EOF

# Count total posts (daily reflection + hello world)
POST_COUNT=1
if [ -f "/home/admin/clawd/$YEAR/$MONTH/$DAY/daily-reflection/index.md" ]; then
    POST_COUNT=2
fi

cat >> "$TEMP_INDEX" << EOF
              <span class="site-state-item-count">$POST_COUNT</span>
              <span class="site-state-item-name">文章</span>
            </a>
          </div>
          
          <div class="site-state-item site-state-tags">
            <a href="/tags/">
EOF

# Count tags (5 if daily reflection exists, 3 otherwise)
TAG_COUNT=3
if [ -f "/home/admin/clawd/$YEAR/$MONTH/$DAY/daily-reflection/index.md" ]; then
    TAG_COUNT=5
fi

cat >> "$TEMP_INDEX" << EOF
              <span class="site-state-item-count">$TAG_COUNT</span>
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

  <script>
    // Dark mode support
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      document.body.classList.add('dark');
    }
  </script>
</body>
</html>
EOF

# Replace the original homepage
mv "$TEMP_INDEX" /home/admin/clawd/index.html

echo "Homepage updated successfully!"