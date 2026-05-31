#!/usr/bin/env python3
"""Refresh the real-GitHub-stats badge block in README.md.

Queries the GitHub GraphQL API (via the `gh` CLI, authenticated by the
GH_TOKEN env var in CI) and rewrites the content between the
<!-- STATS:START ... --> and <!-- STATS:END --> markers. Idempotent:
if the numbers are unchanged, the file is left byte-identical.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

USER = "rahulladumor"
README = Path(__file__).resolve().parents[2] / "README.md"

# label -> (badge color, shields logo slug, logo color)
LANG_BADGE = {
    "JavaScript": ("F7DF1E", "javascript", "black"),
    "TypeScript": ("3178C6", "typescript", "white"),
    "Python": ("3776AB", "python", "white"),
    "HCL": ("7B42BC", "terraform", "white"),
    "Go": ("00ADD8", "go", "white"),
    "Shell": ("89E051", "gnubash", "black"),
    "Java": ("007396", "openjdk", "white"),
    "HTML": ("E34F26", "html5", "white"),
    "CSS": ("1572B6", "css3", "white"),
    "PHP": ("777BB4", "php", "white"),
    "Rust": ("000000", "rust", "white"),
    "Ruby": ("CC342D", "ruby", "white"),
}
LANG_LABEL = {"HCL": "Terraform_%2F_HCL"}


def gh_graphql(query: str) -> dict:
    out = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query}"],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)["data"]


def fetch():
    q = (
        'query{user(login:"%s"){'
        "repositories(ownerAffiliations:OWNER,privacy:PUBLIC,first:100){"
        "totalCount nodes{primaryLanguage{name}}}"
        "contributionsCollection{totalCommitContributions "
        "contributionCalendar{totalContributions}}}}" % USER
    )
    d = gh_graphql(q)["user"]
    repos = d["repositories"]["totalCount"]
    commits = d["contributionsCollection"]["totalCommitContributions"]
    contrib = d["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    langs = {}
    for n in d["repositories"]["nodes"]:
        pl = n.get("primaryLanguage")
        if pl and pl.get("name"):
            langs[pl["name"]] = langs.get(pl["name"], 0) + 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:6]
    return repos, commits, contrib, [k for k, _ in top]


def lang_badge(lang: str) -> str:
    color, logo, lc = LANG_BADGE.get(lang, ("555555", "", "white"))
    label = LANG_LABEL.get(lang, lang.replace(" ", "_"))
    logo_q = f"&logo={logo}&logoColor={lc}" if logo else ""
    return (f'  <img src="https://img.shields.io/badge/{label}-{color}'
            f'?style=flat-square{logo_q}"/>')


def build_block(repos, commits, contrib, langs) -> str:
    lang_imgs = "\n".join(lang_badge(l) for l in langs)
    return (
        "<!-- STATS:START (auto-updated weekly by .github/workflows/update-stats.yml) -->\n"
        '<p align="center">\n'
        f'  <img alt="Contributions in the last year" src="https://img.shields.io/badge/Contributions_·_last_year-{contrib}-2ea043?style=for-the-badge&logo=github&logoColor=white"/>\n'
        f'  <img alt="Commits in the last year" src="https://img.shields.io/badge/Commits_·_last_year-{commits}-667eea?style=for-the-badge&logo=git&logoColor=white"/>\n'
        f'  <img alt="Public repositories" src="https://img.shields.io/badge/Public_Repos-{repos}-764ba2?style=for-the-badge&logo=github&logoColor=white"/>\n'
        "</p>\n"
        "\n"
        "<sub><b>Most-used languages</b></sub>\n"
        "\n"
        '<p align="center">\n'
        f"{lang_imgs}\n"
        "</p>\n"
        "<!-- STATS:END -->"
    )


def main():
    repos, commits, contrib, langs = fetch()
    block = build_block(repos, commits, contrib, langs)
    text = README.read_text(encoding="utf-8")
    pattern = re.compile(r"<!-- STATS:START.*?<!-- STATS:END -->", re.DOTALL)
    if not pattern.search(text):
        print("ERROR: STATS markers not found in README.md", file=sys.stderr)
        sys.exit(1)
    new = pattern.sub(lambda _: block, text)
    if new == text:
        print("stats unchanged")
        return
    README.write_text(new, encoding="utf-8")
    print(f"stats updated: contrib={contrib} commits={commits} repos={repos} langs={langs}")


if __name__ == "__main__":
    main()
