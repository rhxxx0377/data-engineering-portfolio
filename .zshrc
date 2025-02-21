# システムレベルのエイリアスをクリア
unalias python 2>/dev/null || true
unalias python3 2>/dev/null || true

# pyenvの設定を最優先に
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

# pythonコマンドを関数として定義（最も優先度が高い）
function python() {
    command "$PYENV_ROOT/versions/$(pyenv version-name)/bin/python" "$@"
}

# python3コマンドも同様に定義
function python3() {
    command "$PYENV_ROOT/versions/$(pyenv version-name)/bin/python3" "$@"
} 