# Cartesian product function as defined in linear-algebra package

function retval = cartProd (varargin)
  if (nargin < 1)
    print_usage ();
  elseif (nargin == 1)
    retval = varargin{1};
  endif

  [retval{1:nargin}] = ndgrid (varargin{:});
  retval = cat (nargin+1, retval{:});
  retval = reshape (retval, [], nargin);
endfunction
