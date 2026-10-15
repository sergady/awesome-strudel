### U

- `uid`
- `undegrade`
- `undegradeBy`
- `unison`
- `unit`
- `useRNG`

## Entries

### uid

**Call:** `.uid(id)`.

Registered with the playback-metadata controls. This checkout does not apply it.

```js
note("c4").s("triangle").uid(1).gain(0.2)
```

Source: `packages/core/controls.mjs`.

### undegrade

**Call:** `.undegrade()`.

Inverse of `degrade`: Randomly removes 50% of events from the pattern. Shorthand for `.undegradeBy(0.5)`
Events that would be removed by degrade are let through by undegrade and vice versa (see second example).

```js
s("hh*8").undegrade()
```

```js
s("hh*10").layer(
  x => x.degrade().pan(0),
  x => x.undegrade().pan(1)
)
```

Source: `packages/core/signal.mjs`.

### undegradeBy

**Call:** `.undegradeBy(amount)`.

Inverse of `degradeBy`: Randomly removes events from the pattern by a given amount.
0 = 100% chance of removal
1 = 0% chance of removal
Events that would be removed by degradeBy are let through by undegradeBy and vice versa (see second example).

```js
s("hh*8").undegradeBy(0.2)
```

```js
s("hh*10").layer(
  x => x.degradeBy(0.2).pan(0),
  x => x.undegradeBy(0.8).pan(1)
)
```

Source: `packages/core/signal.mjs`.

### unison

**Call:** `.unison(numvoices)`.

Set number of stacked voices for supported oscillators.

```js
note("d f a a# a d3").fast(2).s("supersaw").unison("<1 2 7>")
```

Source: `packages/core/controls.mjs`.

### unit

**Call:** `.unit(unit)`.

Used in conjunction with `speed`, accepts values of "r" (rate, default behavior), "c" (cycles), or "s" (seconds). Using `unit "c"` means `speed` will be interpreted in units of cycles, e.g. `speed "1"` means samples will be stretched to fill a cycle. Using `unit "s"` means the playback speed will be adjusted so that the duration is the number of seconds specified by `speed`.

```js
speed("1 2 .5 3").s("bd").unit("c").osc()
```

Source: `packages/core/controls.mjs`.

### useRNG

**Call:** `useRNG(mod)`.

Sets which random number generator to use. Historically Strudel would
use `useRNG('legacy')`, which remains the default. To use a new more statistically
precise RNG, try `useRNG('precise')`.

```js
useRNG('legacy')
// Repeats every 300 cycles
$: n(irand(50)).seg(16).scale("C:minor").ribbon(88, 32)
$: n(irand(50)).seg(16).scale("C:minor").ribbon(388, 32)
```

Source: `packages/core/signal.mjs`.
