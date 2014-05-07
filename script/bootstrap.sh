#!/bin/bash

set -e

ME=$(basename $0)
DOTFILES_ROOT="$(dirname $(readlink -f ${ME}))"

success() {
	printf "\r\033[2K [\033[00;32mOK\033[0m] $1\n"
}

fail() {
	printf "\r\033[2K [\033[00;31mFAIL\033[0m] $1\n"
	echo ''
	exit
}

link_files() {
	ln -sf $1 $2
	success "linked $1 to $2"
}

install_dotfiles() {
	for source in $(find $DOTFILES_ROOT -maxdepth 2 -name \*.symlink); do
		dest="$HOME/.$(basename ${source%.*})"
		if [ -d $source ]; then
			rm -rf $dest
			source=$source/
		fi
		link_files $source $dest
	done
}

main() {
	install_dotfiles
}

main
