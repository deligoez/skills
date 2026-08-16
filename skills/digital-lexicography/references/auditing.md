# Auditing

Two audits, run around the build rather than after it, and neither uses a model:

```
character audit   BEFORE  — a mapping that no longer holds would bake a wrong reading into
                            every row of the rebuild
build                     — deterministic, offline
parsing audit     AFTER   — checks the database that was just built
```

Running the character audit first is the whole point: it is cheaper to refuse to build than to
discover afterwards that 250,000 rows carry a wrong letter.

## Coverage cannot be circular

The trap is comfortable and almost invisible: you measure parsed codes against your own abbreviation
table, and a code that entered the table *because you saw it in the data* is covered by
construction. The number only ever goes up, and it proves nothing.

Measure against the **source's own printed key** instead, and report two numbers:

```
                     printed   +corpus   unrecognised
etymology_lang        98.1%     99.6%       0.39%   of 63,444 rows
```

- **printed** — the share resting on a code the author himself published. This one cannot be moved
  by editing your own tables, which is exactly why it is the useful one.
- **+corpus** — printed plus codes you have observed and named yourself.
- **unrecognised** — in neither. This is the shortlist to investigate.

Keep the two key sets apart in code: `printed_codes()` and `known_codes()`. Anything you add from
observation goes only in the second.

**Do not gate on the printed share reaching 100%.** Printed keys are provably incomplete — real
dictionaries use codes they never list. Gate on a **floor per column**, recorded from a known-good
build. Adding an observed code leaves the printed share exactly where it was, so a drop cannot be
hidden by growing the list.

## Source occurrence versus parsed occurrence

The generalised question behind "why does this filter have only one entry?":

> For each code the source prints, how often does the source *use* it, and how often did we *parse*
> it?

A code used 140 times and parsed 0 times is a bug. A code used once and parsed once is the
dictionary. Run it over every parsed column; the shortlist is short and each item resolves quickly.

Expect false alarms and check them before acting. `meyve.` looked like 142 uses and 0 parses — but
"meyve" is an ordinary word and every hit was a definition ending in *"…gibi meyve."* Position
matters: a code only counts as a code where the notation puts it.

## Near-duplicate values

The other direction: is one code split across several filter values? Group every facet value by a
folded form — case, diacritics, spaces and dots removed — and report the collisions.

Deliberately over-report. The list is short enough to read, and the false positives are informative.
In one corpus this found eight collisions in a single column and none anywhere else, which is itself
a useful result: the parser was consistent, the source was not.

## Invariants

Shapes that must hold whatever the source says. The valuable ones are relational — they compare two
things that were derived independently:

- A parsed field cannot exist where the field it was parsed from is absent.
- A recognised code, once written to its column, must have **left** the definition text. (7,590
  wrong senses.)
- Denormalised counters agree with the tables they summarise.
- No dangling reference: every link target exists.
- Ordering keys stay inside the alphabet they were built from. A re-scrape that introduces one new
  punctuation mark breaks sorting **silently** — everything with that character piles up past "z"
  and nothing errors.
- Two representations of one fact agree: a display column and its relation table cannot disagree
  about whether a value exists.
- Precomputed page data matches what it summarises. A built statistics page can go stale in a way a
  served one cannot — a number that was right when written stays on screen after the data moves
  under it.

Write invariants as counts that must be zero, and print the count even when it passes. A check that
only speaks when it fails teaches you nothing about the shape of the data.

## Shape

Distribution sanity, cheap and surprisingly effective. A parse that collapses — suddenly every entry
is a noun, or the word class is filled for 3% of entries — is still valid row by row. Only the shape
of the whole reveals it. Print the totals, the fill rates, and the most common value per column on
every build.

## Distrust the measuring tool

Every measurement in this work has a tool between you and the fact, and the tool has its own bugs.
Symptoms worth recognising:

- A headless browser that will not size below a floor, cropping a wide layout and showing overflow
  that does not exist. Measure the layout in something with its own viewport, or compute from
  metrics instead.
- `grep -c` counts *lines*, and server-rendered HTML is often one line. Every query looked like it
  returned one result.
- A stale process serving a database file that has already been replaced on disk. The old inode
  stays open; the numbers are from the previous build.
- A placeholder left in a query. `WHERE x REGEXP 'x'` ran and matched every row containing the
  letter x, producing a confident and entirely meaningless report.

When a result surprises you, re-measure a different way **before** changing any code. Roughly half
the surprises in this kind of work are the instrument.
