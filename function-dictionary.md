# Strudel function dictionary

Alphabetical catalog of the functions you can call from a pattern in this checkout. Names come from `register`, `registerControl`, and `@name` in `packages/`. Regenerate the index with:

```sh
node docs/learning/_extract-functions.mjs
```

There are 596 primary functions and 137 aliases (733 names). Alias lines point at the primary function. Editor color themes are omitted. The [basic function dictionary](basic-functions-dictionary.md) is the shorter listening guide for the core set; entries below are filled one function at a time.

Unless an example sets tempo, evaluate `setcpm(120 / 4)` first. A cycle is Strudel's repeating time unit. At 30 cycles per minute, each cycle lasts two seconds.

**Progress:** letter files are complete through **Z**. [A](Dictionary/A.md) and [B](Dictionary/B.md) are hand-written listening notes. C–Z copy the description and example from the source when the code has them. The browsable site is the single page in `docs/index.html`. Rebuild its data with `python3 scripts/build-site.py`.

- [A](Dictionary/A.md)
- [B](Dictionary/B.md)
- [C](Dictionary/C.md)
- [D](Dictionary/D.md)
- [E](Dictionary/E.md)
- [F](Dictionary/F.md)
- [G](Dictionary/G.md)
- [H](Dictionary/H.md)
- [I](Dictionary/I.md)
- [J](Dictionary/J.md)
- [K](Dictionary/K.md)
- [L](Dictionary/L.md)
- [M](Dictionary/M.md)
- [N](Dictionary/N.md)
- [O](Dictionary/O.md)
- [P](Dictionary/P.md)
- [R](Dictionary/R.md)
- [S](Dictionary/S.md)
- [T](Dictionary/T.md)
- [U](Dictionary/U.md)
- [V](Dictionary/V.md)
- [W](Dictionary/W.md)
- [X](Dictionary/X.md)
- [Z](Dictionary/Z.md)

## Index

### A

- `absoluteOrientationAlpha`
- `absoluteOrientationBeta`
- `absoluteOrientationGamma`
- `absoluteOrientationX` — alias of `absoluteOrientationBeta`
- `absoluteOrientationY` — alias of `absoluteOrientationGamma`
- `absoluteOrientationZ` — alias of `absoluteOrientationAlpha`
- `absOriA` — alias of `absoluteOrientationAlpha`
- `absOriB` — alias of `absoluteOrientationBeta`
- `absOriG` — alias of `absoluteOrientationGamma`
- `absOriX` — alias of `absoluteOrientationBeta`
- `absOriY` — alias of `absoluteOrientationGamma`
- `absOriZ` — alias of `absoluteOrientationAlpha`
- `accelerate`
- `accelerationX`
- `accelerationY`
- `accelerationZ`
- `accX` — alias of `accelerationX`
- `accY` — alias of `accelerationY`
- `accZ` — alias of `accelerationZ`
- `activeLabel`
- `ad`
- `add`
- `addVoicings`
- `adsr`
- `almostAlways`
- `almostNever`
- `always`
- `amp`
- `analyze`
- `anchor`
- `and`
- `apply`
- `applyN`
- `ar`
- `arp`
- `arpWith`
- `as`
- `asym`
- `att` — alias of `attack`
- `attack`

### B

- `band`
- `bandf`
- `bandq`
- `bank`
- `base`
- `bb` — alias of `byteBeatExpression`
- `bbexpr` — alias of `byteBeatExpression`
- `bbst` — alias of `byteBeatStartTime`
- `beat`
- `begin`
- `berlin`
- `bgain` — alias of `busgain`
- `binary`
- `binaryL`
- `binaryN`
- `binaryNL`
- `binshift`
- `bite`
- `bjork`
- `blshift`
- `bmod`
- `bor`
- `bp` — alias of `bpf`
- `bpa` — alias of `bpattack`
- `bpattack`
- `bpd` — alias of `bpdecay`
- `bpdc`
- `bpdecay`
- `bpdepth`
- `bpdepthfreq` — alias of `bpdepthfrequency`
- `bpdepthfrequency`
- `bpe` — alias of `bpenv`
- `bpenv`
- `bpf`
- `bpq`
- `bpr` — alias of `bprelease`
- `bprate`
- `bprelease`
- `bps` — alias of `bpsustain`
- `bpshape`
- `bpskew`
- `bpsustain`
- `bpsync`
- `brak`
- `brand`
- `brandBy`
- `brshift`
- `bus`
- `busgain`
- `bxor`
- `bypass`
- `byteBeatExpression`
- `byteBeatStartTime`

### C

- `ccn`
- `ccv`
- `ceil`
- `ch` — alias of `channels`
- `channel`
- `channels`
- `chebyshev`
- `chop`
- `chord`
- `chorus`
- `chunk`
- `chunkBack`
- `chunkback`
- `chunkBackInto`
- `chunkbackinto`
- `chunkInto`
- `chunkinto`
- `clearScope`
- `clip`
- `coarse`
- `color`
- `colour`
- `comb`
- `compress`
- `compressor`
- `compressorAttack`
- `compressorKnee`
- `compressorRatio`
- `compressorRelease`
- `compressSpan`
- `compressspan`
- `control`
- `cpm`
- `cps`
- `crush`
- `csound`
- `csoundm`
- `ctf` — alias of `lpf`
- `ctlNum`
- `ctranspose`
- `cubic`
- `curve`
- `cut`
- `cutoff`
- `cycleStruct`
- `cyclestruct`

### D

- `datt` — alias of `duckattack`
- `dec` — alias of `decay`
- `decay`
- `degrade`
- `degradeBy`
- `degradeByWith`
- `degree`
- `delay`
- `delayfb` — alias of `delayfeedback`
- `delayfeedback`
- `delays` — alias of `delaysync`
- `delayspeed`
- `delaysync`
- `delayt` — alias of `delayspeed`
- `delaytime`
- `deltaSlide`
- `density`
- `det` — alias of `detune`
- `detune`
- `dfb` — alias of `delayfeedback`
- `dictionary`
- `diode`
- `dist` — alias of `distort`
- `distort`
- `distortion` — alias of `distortvol`
- `distorttype`
- `distortvol`
- `disttype` — alias of `distorttype`
- `distvol` — alias of `distortvol`
- `div`
- `djf`
- `dough`
- `drive`
- `dry`
- `ds`
- `dt` — alias of `delayspeed`
- `duck` — alias of `duckorbit`
- `duckatt` — alias of `duckattack`
- `duckattack`
- `duckdepth`
- `duckons` — alias of `duckonset`
- `duckonset`
- `duckorbit`
- `dur` — alias of `duration`
- `duration`

### E

- `early`
- `echo`
- `echoWith`
- `echowith`
- `edoScale`
- `eish`
- `end`
- `enhance`
- `env`
- `eq`
- `eqt`
- `euclid`
- `euclidish`
- `euclidLegato`
- `euclidLegatoRot`
- `euclidRot`
- `euclidrot`
- `every`
- `expression`

### F

- `fadeInTime`
- `fadeOutTime` — alias of `fadeTime`
- `fadeTime`
- `fanchor`
- `fast`
- `fastChunk`
- `fastchunk`
- `fastGap`
- `fastgap`
- `fft`
- `filter`
- `filterWhen`
- `firstOf`
- `fit`
- `floor`
- `flux`
- `fluxBy`
- `fluxby`
- `fm`
- `fmatt` — alias of `fmattack`
- `fmattack`
- `fmdec` — alias of `fmdecay`
- `fmdecay`
- `fme` — alias of `fmenv`
- `fmenv`
- `fmh`
- `fmi`
- `fmrel` — alias of `fmrelease`
- `fmrelease`
- `fmsus` — alias of `fmsustain`
- `fmsustain`
- `fmwave`
- `focus`
- `focusSpan`
- `focusspan`
- `fold`
- `frameRate`
- `frames`
- `freeze`
- `freq`
- `fromBipolar`
- `fscope`
- `fshift`
- `fshiftnote`
- `fshiftphase`
- `ftrans`
- `fTrans`
- `ftranspose`
- `fTranspose`
- `ftype`
- `FX`
- `FXrelease`

### G

- `gain`
- `gap`
- `gate`
- `getClockTime`
- `getCps`
- `getDuration`
- `getFreq` — alias of `getFrequency`
- `getFrequency`
- `getTime`
- `glide`
- `gravityX`
- `gravityY`
- `gravityZ`
- `gravX` — alias of `gravityX`
- `gravY` — alias of `gravityY`
- `gravZ` — alias of `gravityZ`
- `group`
- `groupmod`
- `grow`
- `gt`
- `gte`

### H

- `hard`
- `harmonic`
- `hbrick`
- `hcutoff`
- `hold`
- `hours`
- `hp` — alias of `hpf`
- `hpa` — alias of `hpattack`
- `hpattack`
- `hpd` — alias of `hpdecay`
- `hpdc`
- `hpdecay`
- `hpdepth`
- `hpdepthfreq` — alias of `hpdepthfrequency`
- `hpdepthfrequency`
- `hpe` — alias of `hpenv`
- `hpenv`
- `hpf`
- `hpq`
- `hpr` — alias of `hprelease`
- `hprate`
- `hprelease`
- `hps` — alias of `hpsustain`
- `hpshape`
- `hpskew`
- `hpsustain`
- `hpsync`
- `hresonance`
- `hsl`
- `hsla`
- `hurry`

### I

- `i`
- `imag`
- `inhabit`
- `inhabitmod`
- `initDough`
- `inside`
- `into`
- `inv`
- `invert`
- `ir`
- `irand`
- `irbegin`
- `iresponse`
- `irspeed`
- `isobite`
- `iter`
- `iterBack`
- `iterback`

### J

- `jux`
- `juxBy`
- `juxby`
- `juxFlip`
- `juxflip`
- `juxFlipBy`
- `juxflipby`

### K

- `K`
- `kcutoff`
- `keep`
- `keyDown`
- `krush`

### L

- `label`
- `lastOf`
- `late`
- `layer`
- `lbrick`
- `legato` — alias of `clip`
- `leslie`
- `lfo`
- `linger`
- `lock`
- `log`
- `log2`
- `logValues`
- `loop`
- `loopAt`
- `loopat`
- `loopAtCps`
- `loopatcps`
- `loopb` — alias of `loopBegin`
- `loopBegin`
- `loope` — alias of `loopEnd`
- `loopEnd`
- `lp` — alias of `lpf`
- `lpa` — alias of `lpattack`
- `lpattack`
- `lpd` — alias of `lpdecay`
- `lpdc`
- `lpdecay`
- `lpdepth`
- `lpdepthfreq` — alias of `lpdepthfrequency`
- `lpdepthfrequency`
- `lpe` — alias of `lpenv`
- `lpenv`
- `lpf`
- `lpq`
- `lpr` — alias of `lprelease`
- `lprate`
- `lprelease`
- `lps` — alias of `lpsustain`
- `lpshape`
- `lpskew`
- `lpsustain`
- `lpsync`
- `lrate`
- `lsize`
- `lt`
- `lte`

### M

- `markcss`
- `midibend`
- `midichan`
- `midicmd`
- `midikeys`
- `midimap`
- `midin`
- `midiport`
- `miditouch`
- `minutes`
- `mod`
- `mode`
- `mousex`
- `mouseX` — alias of `mousex`
- `mousey`
- `mouseY` — alias of `mousey`
- `moveXY`
- `mtranspose`
- `mul`

### N

- `n`
- `ne`
- `net`
- `never`
- `noise`
- `note`
- `nrpnn`
- `nrpv`
- `nudge`

### O

- `o` — alias of `orbit`
- `oct` — alias of `octave`
- `octave`
- `octaveR`
- `octaves`
- `octer`
- `octersub`
- `octersubsub`
- `off`
- `offset`
- `often`
- `onSchedule`
- `onTriggerTime`
- `or`
- `orbit`
- `oriA` — alias of `orientationAlpha`
- `oriB` — alias of `orientationBeta`
- `orientationAlpha`
- `orientationBeta`
- `orientationGamma`
- `orientationX` — alias of `orientationBeta`
- `orientationY` — alias of `orientationGamma`
- `orientationZ` — alias of `orientationAlpha`
- `oriG` — alias of `orientationGamma`
- `oriX` — alias of `orientationBeta`
- `oriY` — alias of `orientationGamma`
- `oriZ` — alias of `orientationAlpha`
- `osc`
- `oschost`
- `oscport`
- `outside`
- `overgain`
- `overshape`

### P

- `pace`
- `palindrome`
- `pan`
- `panchor`
- `panorient`
- `panspan`
- `pansplay`
- `panwidth`
- `parray`
- `partials`
- `patt` — alias of `pattack`
- `pattack`
- `pcurve`
- `pdec` — alias of `pdecay`
- `pdecay`
- `penv`
- `perlin`
- `ph` — alias of `phaser`
- `phasdp` — alias of `phaserdepth`
- `phaser`
- `phasercenter`
- `phaserdepth`
- `phaserrate`
- `phasersweep`
- `phases`
- `phc` — alias of `phasercenter`
- `phd` — alias of `phaserdepth`
- `phs` — alias of `phasersweep`
- `pianoroll`
- `pick`
- `pickF`
- `pickmod`
- `pickmodF`
- `pickmodOut`
- `pickmodReset`
- `pickmodRestart`
- `pickmodSqueeze`
- `pickOut`
- `pickReset`
- `pickRestart`
- `pickSqueeze`
- `pitchJump`
- `pitchJumpTime`
- `pitchwheel`
- `ply`
- `plyForEach`
- `plyforeach`
- `plyWith`
- `plywith`
- `polyTouch`
- `postgain`
- `pow`
- `prel` — alias of `prelease`
- `prelease`
- `press`
- `pressBy`
- `progNum`
- `psustain`
- `punchcard` — alias of `pianoroll`
- `pw`
- `pwr` — alias of `pwrate`
- `pwrate`
- `pws` — alias of `pwsweep`
- `pwsweep`

### R

- `rand`
- `randL`
- `range`
- `range2`
- `rangex`
- `rarely`
- `ratio`
- `rdim` — alias of `roomdim`
- `real`
- `rel` — alias of `release`
- `release`
- `repeatCycles`
- `rescale`
- `resonance`
- `rev`
- `revv`
- `rfade` — alias of `roomfade`
- `rib`
- `ribbon`
- `ring`
- `ringdf`
- `ringf`
- `rlp` — alias of `roomlp`
- `room`
- `roomdim`
- `roomfade`
- `roomlp`
- `roomsize`
- `rootNotes`
- `rotA` — alias of `rotationAlpha`
- `rotationAlpha`
- `rotationBeta`
- `rotationGamma`
- `rotationX` — alias of `rotationBeta`
- `rotationY` — alias of `rotationGamma`
- `rotationZ` — alias of `rotationAlpha`
- `rotB` — alias of `rotationBeta`
- `rotG` — alias of `rotationGamma`
- `rotX` — alias of `rotationBeta`
- `rotY` — alias of `rotationGamma`
- `rotZ` — alias of `rotationAlpha`
- `round`
- `rsize` — alias of `roomsize`

### S

- `s`
- `scale`
- `scaleTrans`
- `scaleTranspose`
- `scope`
- `scram`
- `scramble`
- `scrub`
- `seconds`
- `seed`
- `seg`
- `segment`
- `semitone`
- `sequence`
- `set`
- `setcpm`
- `setGainCurve`
- `setMaxPolyphony`
- `shape`
- `shapevol`
- `shrink`
- `shuffle`
- `signal`
- `silence`
- `sinefold`
- `size`
- `slice`
- `slide`
- `slider`
- `slow`
- `slowChunk`
- `slowchunk`
- `smear`
- `soft`
- `someCycles`
- `someCyclesBy`
- `sometimes`
- `sometimesBy`
- `songPtr`
- `sound` — alias of `s`
- `source`
- `sparsity`
- `speak`
- `spectrum`
- `speed`
- `spiral`
- `splice`
- `spread`
- `squiz`
- `src` — alias of `source`
- `stackCenter`
- `stackCentre` — alias of `stackCenter`
- `stackLeft`
- `stackRepeat`
- `stackRight`
- `stepcat`
- `stepsPerOctave`
- `strans`
- `stretch`
- `striate`
- `stut`
- `stutWith`
- `stutwith`
- `sub`
- `superimpose`
- `sus` — alias of `sustain`
- `sustain`
- `sustainpedal`
- `swing`
- `swingBy`
- `sysex`
- `sysexdata`
- `sysexid`
- `sz` — alias of `roomsize`

### T

- `tables`
- `tag`
- `timeCat` — alias of `stepcat`
- `timecat` — alias of `stepcat`
- `timeline`
- `toBipolar`
- `trans`
- `transient`
- `transpose`
- `transsustain`
- `trem` — alias of `tremolo`
- `tremdepth` — alias of `tremolodepth`
- `tremolo`
- `tremolodepth`
- `tremolophase`
- `tremoloshape`
- `tremoloskew`
- `tremolosync`
- `tremphase` — alias of `tremolophase`
- `tremshape` — alias of `tremoloshape`
- `tremskew` — alias of `tremoloskew`
- `tremsync` — alias of `tremolosync`
- `triode`
- `tscope` — alias of `scope`
- `tsdelay`
- `tune`
- `tuning`

### U

- `uid`
- `undegrade`
- `undegradeBy`
- `unison`
- `unit`
- `useRNG`

### V

- `v` — alias of `vib`
- `val`
- `vel` — alias of `velocity`
- `velocity`
- `vib`
- `vibmod`
- `vibrato` — alias of `vib`
- `vlpf`
- `vmod` — alias of `vibmod`
- `voice`
- `voices`
- `voicing`
- `voicings`
- `vowel`

### W

- `warp`
- `warpatt` — alias of `warpattack`
- `warpattack`
- `warpdc`
- `warpdec` — alias of `warpdecay`
- `warpdecay`
- `warpdepth`
- `warpenv`
- `warpmode`
- `warprate`
- `warprel` — alias of `warprelease`
- `warprelease`
- `warpshape`
- `warpskew`
- `warpsus` — alias of `warpsustain`
- `warpsustain`
- `warpsync`
- `waveloss`
- `wavetablePhaseRand` — alias of `wtphaserand`
- `wavetablePosition` — alias of `wt`
- `wavetableWarp` — alias of `warp`
- `wavetableWarpMode` — alias of `warpmode`
- `weave`
- `weaveWith`
- `when`
- `whenKey`
- `withBase`
- `within`
- `wordfall`
- `worklet`
- `wt`
- `wtatt` — alias of `wtattack`
- `wtattack`
- `wtdc`
- `wtdec` — alias of `wtdecay`
- `wtdecay`
- `wtdepth`
- `wtenv`
- `wtphaserand`
- `wtrate`
- `wtrel` — alias of `wtrelease`
- `wtrelease`
- `wtshape`
- `wtskew`
- `wtsus` — alias of `wtsustain`
- `wtsustain`
- `wtsync`

### X

- `xen`
- `xfade`
- `xsdelay`

### Z

- `zcrush`
- `zdelay`
- `zmod`
- `znoise`
- `zoom`
- `zoomArc`
- `zoomarc`
- `zoomIn`
- `zrand`
- `zzfx`
