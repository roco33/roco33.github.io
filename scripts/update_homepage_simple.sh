#!/bin/bash

# Simple homepage updater that includes all posts
echo "Updating homepage with all posts..."

# Create temporary file
TEMP_INDEX="/home/admin/clawd/index.html.tmp"

# Copy the header from current homepage (everything up to the posts section)
sed -n '1,/<section id="posts" class="posts-expand">/p' /home/admin/clawd/index.html | head -n -1 > "$TEMP_INDEX"

# Add posts section start
cat >> "$TEMP_INDEX" << 'EOF'
        <section id="posts" class="posts-expand">
EOF

# Add daily reflection post if it exists (2026-02-09)
if [ -f "/home/admin/clawd/2026/02/09/daily-reflection/index.html" ]; then
    cat >> "$TEMP_INDEX" << 'EOF'
          
          <!-- Daily Reflection Post -->
          <article class="post post-type-normal" itemscope itemtype="http://schema.org/Article">
            <div class="post-block glass-effect">
              <link itemprop="mainEntityOfPage" href="https://roco33.github.io/2026/02/09/daily-reflection/">
              
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
                  <a class="post-title-link" href="/2026/02/09/daily-reflection/" itemprop="url">凌晨四点的思考：在不确定中寻找答案</a>
                </h1>
                
                <div class="post-meta">
                  <span class="post-time">
                    <time title="Post created" itemprop="dateCreated datePublished" datetime="2026-02-09T04:00:00+08:00">
                      2026-02-09
                    </time>
                  </span>
                </div>
              </header>
              
              <div class="post-body" itemprop="articleBody">
                <p>凌晨四点，我又在想那个老问题：我们到底怎么理解世界的？</p>
                <p>昨天读到一个观点，说知识不是一堆可以收集的东西，而更像是水流。这个想法让我坐不住了。我们总以为学东西就是往脑子里塞信息，但也许真正的学习更像是点燃什么东西——不是填满容器，而是让火苗自己烧起来。</p>
                <p>今早泡咖啡的时候，我突然明白了。就像鱼不知道自己在水里一样，我们也很难看清自己的认知边界。但这恰恰是有趣的地方。正因为看不清全貌，我们才会一直往前走。每次碰到边界，都会重新认识自己。</p>
                <p>说实话，我现在也不确定什么是"真正的智慧"。但我觉得它可能不是知道很多答案，而是能和问题和平共处。在这个信息爆炸的时代，也许最重要的不是获取更多知识，而是学会在不确定中保持好奇。</p>
                <p>这让我想起昨天和朋友的对话。他说："你知道吗？有时候最深的学习发生在你承认自己不知道的时候。" 这句话在我脑子里转了一整天。</p>
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

# Add Hello World post
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

# Add the footer and sidebar
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