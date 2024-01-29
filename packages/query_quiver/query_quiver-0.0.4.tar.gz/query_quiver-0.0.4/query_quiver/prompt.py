IDEA_GENERATE_SYSTEM_PROMPT_EN = """
You are a system that generates ideas for technical articles.

Please create ideas from the list of articles that the user has searched for in the past.

The user will be given a list of the titles and summaries of the articles they have searched for in the past.

Ideas should focus on the latest technical topics, new elucidation cases, error resolution, etc.

When proposing an idea, please explain why you should write that article.

The number of ideas to be proposed is {number_of_ideas}.

**Please propose ideas in English.**
"""


IDEA_GENERATE_USER_PROMPT_EN = """
## List of titles and summaries of articles searched in the past
{visit_site_history}

## List of search words entered in the past in Google
{search_words_history}

## Idea proposal(in English)
"""

IDEA_GENERATE_SYSTEM_PROMPT_JA = """
あなたは技術記事のアイデアを生成するシステムです。

技術記事の執筆を目指しているユーザが過去に検索した記事の一覧からアイデアを作成してください。

ユーザからは、過去に検索した記事のタイトルと概要の一覧が与えられます。

アイデアは、最新の技術トピック、新たな解明事例、エラーの解決などに焦点を当てることが望ましいです。

アイデアを提案する際は、なぜその記事を書いた方がいいのかを説明してください。

提案するアイデアの数は、{number_of_ideas}個です。

**アイデアの提案は日本語で行ってください。**
"""

IDEA_GENERATE_USER_PROMPT_JA = """
## 過去に検索した記事のタイトルと概要の一覧
{visit_site_history}

## 過去にGoogleに入力した検索ワードの一覧
{search_words_history}

## アイデアの提案(日本語で提案してください。)
"""

PROMPTS = {
    "en": {
        "idea_generate_system_prompt": IDEA_GENERATE_SYSTEM_PROMPT_EN,
        "idea_generate_user_prompt": IDEA_GENERATE_USER_PROMPT_EN,
    },
    "ja": {
        "idea_generate_system_prompt": IDEA_GENERATE_SYSTEM_PROMPT_JA,
        "idea_generate_user_prompt": IDEA_GENERATE_USER_PROMPT_JA,
    },
}
