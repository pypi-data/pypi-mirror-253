# implies: a Pybound Rust crate for logical formulas

**implies** is a Rust crate for storing logical formulas as parse trees and performing complex operations on them,
like substitution, rotation, conversion to conjunctive normal form, and more. Propositional logic comes pre-implemented, 
but this crate operates on a generic struct `Formula<B,U,A>` which can easily be used with your own `B`inary and `U`nary
operators and `Atom`ic formula types: if you can implement those types for your own preferred logic (modal, temporal, 
predicate, etc...) you can use the full functionality of this crate for your own language. A lot more information is in
the [docs](https://docs.rs/implies/0.2.1-alpha/implies) for this crate.

There are Python bindings for propositional logic, but using the API in Python gives much less control and flexibility.
You can use the Python APIs from Rust if you want by enabling the "python" feature when compiling, which will add "pyo3" as a dependency.

Here is a simple example of implementing a basic modal logic with implies, so you can see how easily you can use implies for your own logical language:

```rust
use crate::formula::*;
use crate::parser::Match;
use crate::prop::*;
use crate::symbol::{Atom, Symbolic};

/// The usual unary operators for modal logic: negation,
/// box and diamond. Most of the traits you need to get your
/// symbol types to work with implies are derivable.
///
/// Pro tip:
/// Write operator enums like this in the ascending precedence order
/// want for your operators, so that deriving Ord freely gives you the
/// precedence you expect. In the case of unary operators like these,
/// it doesn't matter, but it's useful for binary operators.
#[derive(PartialEq, Eq, Ord, PartialOrd, Copy, Clone, Default, Hash)]
enum ModalUnary {
    Box,
    Diamond,
    // Give any value as the default, it just allows
    // fast swap operations under the hood without
    // unsafe Rust.
    #[default]
    Not,
}

/// Specify how your type should be pretty-printed.
impl std::fmt::Display for ModalUnary {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            ModalUnary::Box => write!(f, "◻"),
            ModalUnary::Diamond => write!(f, "◊"),
            ModalUnary::Not => write!(f, "¬"),
        }
    }
}

/// This marker trait shows you've covered all the bases.
impl Symbolic for ModalUnary {}

/// Implement this simple trait (whose methods are partial inverses)
/// for immediate access to parsing formulae from strings.
impl Match for ModalUnary {
    fn match_str(s: &str) -> Option<Self> {
        match s {
            "◻" => Some(ModalUnary::Box),
            "◊" => Some(ModalUnary::Diamond),
            "¬" | "not" | "~" => Some(ModalUnary::Not),
            _ => None,
        }
    }

    fn get_matches(&self) -> Vec<String> {
        match self {
            ModalUnary::Box => vec!["◻".to_owned()],
            ModalUnary::Diamond => vec!["◊".to_owned()],
            ModalUnary::Not => vec!["¬".to_owned(), "not".to_owned(), "~".to_owned()],
        }
    }
}

/// The binary operators for modal logic are the same as those for propositional.
type ModalBinary = PropBinary;

/// Just write a type alias and that's it, all of implies' functionality for free.
type ModalFormula = Formula<ModalBinary, ModalUnary, Atom>;
```

Once you have a type like `ModalFormula` set up, you can just use all the provided methods
in the Formula struct for free. To initialize a formula you can start with just an atom

```rust
let mut f = ModalFormula::new(Atom("p"))  // p
```

or use the cascade macro for builder syntax

```rust
let mut f = cascade! {
  let f = ModalFormula::new(Atom("p"))   // p
  ..unify(ModalUnary::Box)               // ◻p
  ..left_combine(PropBinary::Implies, ModalFormula::new(Atom("q"))) // q -> ◻p
}
```

or if your type implements `Match` just use a string!

```rust
use implies::parser::build_formula;

let mut f: ModalFormula = build_formula("q -> ◻p")?;
```