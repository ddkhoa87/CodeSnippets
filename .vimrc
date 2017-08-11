filetype plugin indent on
syntax on

" Set the space of tab and indent
set tabstop=4       " The width of a TAB is set to 4.
                    " Still it is a \t. It is just that
		    " Vim will interpret it to be having
		    " a width of 4.
		    "
set shiftwidth=4
		    " Indents will
		    " have a width of
		    " 4
		    "
set softtabstop=4
		    " Sets the
		    " number of
		    " columns for a
		    " TAB
		    "
set expandtab " Expand TABs to spaces

" Code folding
set foldmethod=indent   
set foldnestmax=10
set nofoldenable
set foldlevel=1
