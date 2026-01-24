---
layout: default
title: "脳科学辞典 (Brain Science Dictionary)"
description: "日本神経科学学会が運営する、脳科学に関する用語の解説辞典"
article_type: External Resource
subtitle: "日本神経科学学会が運営する、脳科学に関する用語の解説辞典"
---

    <main class="main-container">
        <article class="content-column">

            <section class="section">
                <h2 class="section-title">Overview</h2>
                <p><strong>脳科学辞典</strong>は、脳科学の広範な分野に関する用語を、専門家が執筆・査読した信頼性の高いオンライン辞典です。本プロジェクト（EEGFlow）では、マインドアップロード（WBE）に関連する神経科学的基盤の理解を深めるための一次リソースとして、この辞典を参照しています。</p>
                <p>以下に、WBE研究において特に重要となる用語へのリンクと、辞典全体の索引へのアクセスを提供します。</p>
            </section>

            <section class="section">
                <h2 class="section-title">Selected Keywords for Mind Uploading</h2>
                <p>マインドアップロード（WBE）の「計測」「再構成」「実装」「検証」の各フェーズに関連する主要な用語です。</p>

                <div class="term-list">
                    <div class="term-item">
                        <a href="https://bsd.neuroinf.jp/wiki/コネクトーム" target="_blank">コネクトーム (Connectome)</a>
                        <span>脳内の神経回路網の全体的な地図。WBEにおける「構造的再構成」の基盤となる概念。</span>
                    </div>
                    <div class="term-item">
                        <a href="https://bsd.neuroinf.jp/wiki/シナプス可塑性" target="_blank">シナプス可塑性 (Synaptic plasticity)</a>
                        <span>神経活動依存的なシナプス伝達効率の変化。学習と記憶の細胞基盤であり、WBEにおける「学習則」の推定に不可欠。</span>
                    </div>
                    <div class="term-item">
                        <a href="https://bsd.neuroinf.jp/wiki/意識" target="_blank">意識 (Consciousness)</a>
                        <span>主観的な体験。統合情報理論（IIT）やグローバルワークスペース理論（GNWT）などの理論的枠組みが含まれる。</span>
                    </div>
                    <div class="term-item">
                        <a href="https://bsd.neuroinf.jp/wiki/脳波" target="_blank">脳波 (Electroencephalogram, EEG)</a>
                        <span>頭皮上から記録される脳の電気活動。本プロジェクトの主要な計測モダリティ。</span>
                    </div>
                    <div class="term-item">
                        <a href="https://bsd.neuroinf.jp/wiki/ブレイン・マシン・インターフェース" target="_blank">ブレイン・マシン・インターフェース (BMI)</a>
                        <span>脳と外部機器を接続する技術。WBEの過渡期における「サイボーグ化」や「段階的置換」に関連。</span>
                    </div>
                    <div class="term-item">
                        <a href="https://bsd.neuroinf.jp/wiki/グリア細胞" target="_blank">グリア細胞 (Glial cell)</a>
                        <span>ニューロン以外の脳細胞。近年、情報処理への関与が指摘されており、WBEにおけるモデル化の必要性が議論されている。</span>
                    </div>
                    <div class="term-item">
                        <a href="https://bsd.neuroinf.jp/wiki/大脳皮質" target="_blank">大脳皮質 (Cerebral cortex)</a>
                        <span>知覚、運動、思考などの高次脳機能を司る領域。WBEの主要なエミュレーション対象。</span>
                    </div>
                    <div class="term-item">
                        <a href="https://bsd.neuroinf.jp/wiki/ニューラルネットワーク" target="_blank">ニューラルネットワーク (Neural network)</a>
                        <span>脳の神経回路網を模した数理モデル。WBEの「実装」基盤として重要。</span>
                    </div>
                </div>
            </section>

            <section class="section" id="full-index">
                <h2 class="section-title">Full Index</h2>
                <p>脳科学辞典の全項目索引を、MediaWiki API から取得して一覧に反映しています。まずはカテゴリ別のショートカットから参照できます。</p>

                <div class="dict-grid">
                    <div class="dict-card">
                        <h4>五十音順索引</h4>
                        <a href="https://bsd.neuroinf.jp/wiki/脳科学辞典:索引" target="_blank">あ - ん</a>
                    </div>
                    <div class="dict-card">
                        <h4>アルファベット索引</h4>
                        <a href="https://bsd.neuroinf.jp/wiki/脳科学辞典:索引" target="_blank">A - Z</a>
                    </div>
                    <div class="dict-card">
                        <h4>数字索引</h4>
                        <a href="https://bsd.neuroinf.jp/wiki/脳科学辞典:索引" target="_blank">0 - 9</a>
                    </div>
                    <div class="dict-card">
                        <h4>分野別一覧</h4>
                        <a href="https://bsd.neuroinf.jp/wiki/Category:分野別" target="_blank">Category List</a>
                    </div>
                </div>

                <div class="bsd-controls">
                    <input id="bsd-search" class="filter-input" type="search" placeholder="辞典内検索（例: 意識, シナプス, EEG）">
                    <span id="bsd-count" class="bsd-count">読み込み中...</span>
                </div>
                <p id="bsd-status" class="bsd-status">索引を読み込み中...</p>
                <ul id="bsd-index" class="bsd-index" hidden></ul>
                <p class="bsd-note">出典: <a href="https://bsd.neuroinf.jp/wiki/脳科学辞典:索引" target="_blank">脳科学辞典</a> (CC BY-NC-SA 4.0)</p>
            </section>

        </article>

        <aside class="sidebar-column">
            <div class="sidebar-box">
                <h4>About BSD</h4>
                <p>脳科学辞典は、日本神経科学学会によって運営されています。本ページは MediaWiki API から索引を取得して表示しています。</p>
                <p>ライセンス: <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja" target="_blank">CC BY-NC-SA 4.0</a></p>
            </div>

            <div class="sidebar-box">
                <h4>Navigation</h4>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="tech_roadmap.html">Technical Roadmap</a></li>
                    <li><a href="mind_uploading_papers.html">Paper Collection</a></li>
                </ul>
            </div>

            <div class="sidebar-box">
                <h4>External Links</h4>
                <ul>
                    <li><a href="https://bsd.neuroinf.jp/" target="_blank">脳科学辞典 Top</a></li>
                    <li><a href="https://www.jnss.org/" target="_blank">日本神経科学学会</a></li>
                </ul>
            </div>
        </aside>
    </main>

    <footer>
        <p>EEGFlow Project · <a href="https://github.com/yasufumi-nakata/eegflow">GitHub</a></p>
    </footer>

    <script>
        (function () {
            var indexEl = document.getElementById('bsd-index');
            var statusEl = document.getElementById('bsd-status');
            var countEl = document.getElementById('bsd-count');
            var searchInput = document.getElementById('bsd-search');
            var titles = [];

            if (!indexEl || !statusEl || !countEl || !searchInput) return;

            function setStatus(message) {
                statusEl.textContent = message;
                statusEl.style.display = message ? 'block' : 'none';
            }

            function updateCount(visible) {
                if (typeof visible === 'number') {
                    countEl.textContent = '表示: ' + visible + ' / ' + titles.length;
                    return;
                }
                countEl.textContent = '全' + titles.length + '件';
            }

            function buildList(items) {
                var fragment = document.createDocumentFragment();
                for (var i = 0; i < items.length; i++) {
                    var title = items[i];
                    var li = document.createElement('li');
                    li.dataset.title = title.toLowerCase();

                    var link = document.createElement('a');
                    link.href = 'https://bsd.neuroinf.jp/wiki/' + encodeURIComponent(title.replace(/ /g, '_'));
                    link.target = '_blank';
                    link.rel = 'noopener noreferrer';
                    link.textContent = title;

                    li.appendChild(link);
                    fragment.appendChild(li);
                }
                indexEl.appendChild(fragment);
            }

            function applyFilter() {
                var query = searchInput.value.trim().toLowerCase();
                var items = indexEl.querySelectorAll('li');
                var visible = 0;

                for (var i = 0; i < items.length; i++) {
                    var item = items[i];
                    var title = item.dataset.title || '';
                    var match = !query || title.indexOf(query) !== -1;
                    item.style.display = match ? '' : 'none';
                    if (match) visible++;
                }

                updateCount(query ? visible : null);
                setStatus(query && visible === 0 ? '該当する項目がありません。' : '');
            }

            function fetchAllPages() {
                var apiBase = 'https://bsd.neuroinf.jp/w/api.php';
                var params = 'action=query&list=allpages&aplimit=500&format=json&origin=*';
                var pages = [];

                function fetchNext(continueToken) {
                    var url = apiBase + '?' + params;
                    if (continueToken) {
                        url += '&apcontinue=' + encodeURIComponent(continueToken);
                    }

                    return fetch(url).then(function (response) {
                        if (!response.ok) {
                            throw new Error('HTTP ' + response.status);
                        }
                        return response.json();
                    }).then(function (data) {
                        var list = data.query && data.query.allpages ? data.query.allpages : [];
                        for (var i = 0; i < list.length; i++) {
                            pages.push(list[i].title);
                        }

                        var nextToken = data.continue && data.continue.apcontinue;
                        if (nextToken) {
                            return fetchNext(nextToken);
                        }
                        return pages;
                    });
                }

                return fetchNext(null);
            }

            setStatus('索引を読み込み中...');
            fetchAllPages().then(function (items) {
                titles = items.slice(0);
                titles.sort(function (a, b) {
                    return a.localeCompare(b, 'ja');
                });
                buildList(titles);
                indexEl.hidden = false;
                setStatus('');
                updateCount();
            }).catch(function (error) {
                console.error('BSD index fetch failed:', error);
                setStatus('索引の取得に失敗しました。直接アクセスしてください。');
                countEl.textContent = '取得失敗';
            });

            searchInput.addEventListener('input', function () {
                if (!titles.length) return;
                applyFilter();
            });
        })();
    </script>
