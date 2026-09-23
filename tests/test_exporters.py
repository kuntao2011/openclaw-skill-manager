# -*- coding: utf-8 -*-
from exporter.markdown import generate_markdown
from exporter.json_exporter import generate_json_data
from exporter.html_exporter import generate_html, build_cols
from data.deps import render_mermaid


def _skills():
    return [
        {'name': 'alpha', 'status': 'ready', 'version': '1.0', 'source': 'openclaw-bundled',
         'emoji': '🔥', 'homepage': 'https://example.com/alpha', 'description': 'd1'},
        {'name': 'beta', 'status': 'needsetup', 'version': '', 'source': 'openclaw-workspace',
         'emoji': '', 'homepage': '', 'description': 'd2'},
    ]


def test_markdown_contains_columns():
    md = generate_markdown(_skills(), 't', usage={'alpha': {'calls': 3, 'last_used': None}})
    assert '来源' in md and '调用量' in md
    assert '[🔥 alpha](https://example.com/alpha)' in md
    assert 'bundled' in md


def test_markdown_without_usage_column():
    md = generate_markdown(_skills(), 't')
    assert '调用量' not in md


def test_markdown_deps_section():
    edges = [{'skill': 'beta', 'dep': 'ffmpeg', 'kind': 'bin'}]
    md = generate_markdown(_skills(), 't', deps_edges=edges)
    assert '缺失依赖关系' in md and 'graph LR' in md


def test_json_data_usage_and_deps():
    data = generate_json_data(_skills(), 't',
                              usage={'alpha': {'calls': 1}}, deps_edges=[])
    assert data['usage'] == {'alpha': {'calls': 1}}
    assert data['dependency_edges'] == []


def test_html_contains_sort_and_svg():
    edges = [{'skill': 'beta', 'dep': 'ffmpeg', 'kind': 'bin'}]
    page = generate_html(_skills(), 't', usage={'alpha': {'calls': 2}}, deps_edges=edges)
    assert 'data-sort' in page and '<svg' in page and 'searchInput' in page


def test_build_cols_order():
    cols = build_cols({'alpha': {'calls': 1}})
    assert [c['key'] for c in cols] == \
        ['status', 'name', 'version', 'source', 'calls', 'category', 'description']
    cols_plain = build_cols(None)
    assert 'calls' not in [c['key'] for c in cols_plain]


def test_mermaid_render():
    src = render_mermaid([{'skill': 'a-b', 'dep': 'ffmpeg', 'kind': 'bin'}])
    assert src.startswith('```mermaid') and 'graph LR' in src
