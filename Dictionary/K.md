### K

- `K`
- `kcutoff`
- `keep`
- `keyDown`
- `krush`

## Entries

### K

**Call:** `.K(expr)`.

Produces a [Kabelsalat](https://kabel.salat.dev/) modular sound engine.
This can be used as either an effect (by including `audioin()` at the beginning
of your kabel expression) or as a sound source (via any expression which doesn't
start with `audioin()`).

Some helpers you have available to you:
  * Strudel mini notation works fine in K(..) via "" or ``
  * More complex Strudel expressions (like "0 1 2".fast(4) or irand(24)) can be
    written by wrapping them in `S(..)` inside your Kabel code
  * We expose Strudel's note frequency under `sFreq` and Strudel's gate
    information under `sGate`
  * You can use more complex multi-line expressions (like `let x = a; let y = b; x.lpf(y);`)
    by wrapping them inside a function in K (see example).

```js
note("A c e".fast(4)).transpose("<0 2 4 6 8>")
  .scale("F:minor").transpose("12")
  .s("saw")
  .K(
    // audioin().mul(sGate.adsr(0.001, 0.3, 0, 0.2)) // as effect
    saw(saw(sFreq / "2!3 16").mul(8).add(sFreq).lag("0!3 0.1")).mul(0.3) // as source
    .mul(sGate.adsr(0, 0.15, 0.5, "0.1!3 1"))
    .lpf(sGate.adsr(0, 0.2, 0.3, 0.2).mul(1).add(0))
    .add(x => x.delay(S("0.3 0.2".fast(2))).mul(0.7))
    .add(x => x.delay("0.03 [0.08 0.01] 0.01 0.013").mul(0.77)).mul(0.7)
    .add(x => x.delay(.13).mul(0.7))
    .out()
  )
```

```js
n("<0 1 <2 3 2 4>>*16")
  .scale("G#2:minor").sometimes(x => x.transpose("12 | 24"))
  .K(() => {
    const att = S(rand.range(0, 0.05))
    const dec = S(rand.range(0.05, 0.2))
    let f = n(sFreq);
    const mod = sine(f).mul("0.1 | 0.2 | 0.3")
      .add("[[1.5 1] | 1 | 2 | 4 | [6 4@3]]*2")
    saw(f.mul(mod))
    .mul(sGate.ad(att, dec))
    .add(x => x.delay(0.4).mul(0.3))
    .out()
  }).fxr(1).room(0.3)
```

Source: `packages/core/pattern.mjs`.

### kcutoff

**Call:** `.kcutoff(frequency)`.

Low-pass cutoff that follows `krush`. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3").s("sawtooth").krush(0.5).kcutoff("<500 4000>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.

### keep

**Call:** `.keep(pat)`.

When called on a pattern `a`, with a input pattern `b` (`a.keep(b)`),
combines `a` and `b` such that anything defined in `a`,
and anything defined in `b` that is *not* defined in `a`
will be in the resulting pattern

The structure is maintained from `a`,
because the default pattern alignment is `in`,
see the section on `Pattern Alignment`
in the technical manual in the docs

This is the inverse of `set`

See examples below

```js
// notes, already defined, will stay "c a f e",
// while "s", not defined, will be set to "piano"
note("c a f e").keep(note("e f a c").s("piano"))
```

Source: `packages/core/pattern.mjs`.

### keyDown

**Call:** `.keyDown(…)`.

returns true when a key or array of keys is held
[Key name reference](https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values)

```js
keyDown("Control:j").pick([s("bd(5,8)"), s("cp(3,8)")])
```

Source: `packages/core/signal.mjs`.

### krush

**Call:** `.krush(amount)`.

Bit-crushing. The browser synth does not read this control. It is registered with the other SuperDirt effects, next to `waveloss`.

```js
note("c3 e3 g3").s("sawtooth").krush("<0 .3 .7>").osc().gain(0.15)
```

Source: `packages/core/controls.mjs`.
