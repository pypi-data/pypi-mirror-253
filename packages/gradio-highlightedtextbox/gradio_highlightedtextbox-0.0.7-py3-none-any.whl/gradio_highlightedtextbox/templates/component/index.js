const {
  SvelteComponent: nl,
  append: se,
  attr: U,
  create_slot: il,
  destroy_each: sl,
  detach: oe,
  element: ce,
  empty: ol,
  ensure_array_like: et,
  get_all_dirty_from_scope: fl,
  get_slot_changes: al,
  init: _l,
  insert: fe,
  safe_not_equal: rl,
  set_data: Ue,
  space: He,
  text: Xe,
  toggle_class: V,
  transition_in: ul,
  transition_out: cl,
  update_slot_base: dl
} = window.__gradio__svelte__internal;
function tt(l, e, t) {
  const n = l.slice();
  return n[8] = e[t][0], n[9] = e[t][1], n[11] = t, n;
}
function lt(l) {
  let e, t, n, i, s, o, r = et(Object.entries(
    /*_color_map*/
    l[4]
  )), _ = [];
  for (let f = 0; f < r.length; f += 1)
    _[f] = nt(tt(l, r, f));
  return {
    c() {
      e = ce("span"), e.textContent = "·", t = He(), n = ce("div"), i = ce("span"), s = Xe(
        /*legend_label*/
        l[3]
      ), o = He();
      for (let f = 0; f < _.length; f += 1)
        _[f].c();
      U(e, "class", "legend-separator svelte-vm3q5z"), V(e, "hide", !/*show_legend*/
      l[1] || !/*show_label*/
      l[0]), V(
        e,
        "has-info",
        /*info*/
        l[5] != null
      ), U(i, "class", "svelte-vm3q5z"), V(i, "hide", !/*show_legend_label*/
      l[2]), V(
        i,
        "has-info",
        /*info*/
        l[5] != null
      ), U(n, "class", "category-legend svelte-vm3q5z"), U(n, "data-testid", "highlighted-text:category-legend"), V(n, "hide", !/*show_legend*/
      l[1]);
    },
    m(f, a) {
      fe(f, e, a), fe(f, t, a), fe(f, n, a), se(n, i), se(i, s), se(n, o);
      for (let u = 0; u < _.length; u += 1)
        _[u] && _[u].m(n, null);
    },
    p(f, a) {
      if (a & /*show_legend, show_label*/
      3 && V(e, "hide", !/*show_legend*/
      f[1] || !/*show_label*/
      f[0]), a & /*info*/
      32 && V(
        e,
        "has-info",
        /*info*/
        f[5] != null
      ), a & /*legend_label*/
      8 && Ue(
        s,
        /*legend_label*/
        f[3]
      ), a & /*show_legend_label*/
      4 && V(i, "hide", !/*show_legend_label*/
      f[2]), a & /*info*/
      32 && V(
        i,
        "has-info",
        /*info*/
        f[5] != null
      ), a & /*Object, _color_map, info*/
      48) {
        r = et(Object.entries(
          /*_color_map*/
          f[4]
        ));
        let u;
        for (u = 0; u < r.length; u += 1) {
          const c = tt(f, r, u);
          _[u] ? _[u].p(c, a) : (_[u] = nt(c), _[u].c(), _[u].m(n, null));
        }
        for (; u < _.length; u += 1)
          _[u].d(1);
        _.length = r.length;
      }
      a & /*show_legend*/
      2 && V(n, "hide", !/*show_legend*/
      f[1]);
    },
    d(f) {
      f && (oe(e), oe(t), oe(n)), sl(_, f);
    }
  };
}
function nt(l) {
  let e, t = (
    /*category*/
    l[8] + ""
  ), n, i, s;
  return {
    c() {
      e = ce("div"), n = Xe(t), i = He(), U(e, "class", "category-label svelte-vm3q5z"), U(e, "style", s = "background-color:" + /*color*/
      l[9].secondary), V(
        e,
        "has-info",
        /*info*/
        l[5] != null
      );
    },
    m(o, r) {
      fe(o, e, r), se(e, n), se(e, i);
    },
    p(o, r) {
      r & /*_color_map*/
      16 && t !== (t = /*category*/
      o[8] + "") && Ue(n, t), r & /*_color_map*/
      16 && s !== (s = "background-color:" + /*color*/
      o[9].secondary) && U(e, "style", s), r & /*info*/
      32 && V(
        e,
        "has-info",
        /*info*/
        o[5] != null
      );
    },
    d(o) {
      o && oe(e);
    }
  };
}
function it(l) {
  let e, t;
  return {
    c() {
      e = ce("div"), t = Xe(
        /*info*/
        l[5]
      ), U(e, "class", "title-with-highlights-info svelte-vm3q5z");
    },
    m(n, i) {
      fe(n, e, i), se(e, t);
    },
    p(n, i) {
      i & /*info*/
      32 && Ue(
        t,
        /*info*/
        n[5]
      );
    },
    d(n) {
      n && oe(e);
    }
  };
}
function ml(l) {
  let e, t, n, i = Object.keys(
    /*_color_map*/
    l[4]
  ).length !== 0, s, o, r;
  const _ = (
    /*#slots*/
    l[7].default
  ), f = il(
    _,
    l,
    /*$$scope*/
    l[6],
    null
  );
  let a = i && lt(l), u = (
    /*info*/
    l[5] && it(l)
  );
  return {
    c() {
      e = ce("div"), t = ce("span"), f && f.c(), n = He(), a && a.c(), s = He(), u && u.c(), o = ol(), U(t, "data-testid", "block-info"), U(t, "class", "svelte-vm3q5z"), V(t, "sr-only", !/*show_label*/
      l[0]), V(t, "hide", !/*show_label*/
      l[0]), V(
        t,
        "has-info",
        /*info*/
        l[5] != null
      ), U(e, "class", "title-container svelte-vm3q5z");
    },
    m(c, m) {
      fe(c, e, m), se(e, t), f && f.m(t, null), se(e, n), a && a.m(e, null), fe(c, s, m), u && u.m(c, m), fe(c, o, m), r = !0;
    },
    p(c, [m]) {
      f && f.p && (!r || m & /*$$scope*/
      64) && dl(
        f,
        _,
        c,
        /*$$scope*/
        c[6],
        r ? al(
          _,
          /*$$scope*/
          c[6],
          m,
          null
        ) : fl(
          /*$$scope*/
          c[6]
        ),
        null
      ), (!r || m & /*show_label*/
      1) && V(t, "sr-only", !/*show_label*/
      c[0]), (!r || m & /*show_label*/
      1) && V(t, "hide", !/*show_label*/
      c[0]), (!r || m & /*info*/
      32) && V(
        t,
        "has-info",
        /*info*/
        c[5] != null
      ), m & /*_color_map*/
      16 && (i = Object.keys(
        /*_color_map*/
        c[4]
      ).length !== 0), i ? a ? a.p(c, m) : (a = lt(c), a.c(), a.m(e, null)) : a && (a.d(1), a = null), /*info*/
      c[5] ? u ? u.p(c, m) : (u = it(c), u.c(), u.m(o.parentNode, o)) : u && (u.d(1), u = null);
    },
    i(c) {
      r || (ul(f, c), r = !0);
    },
    o(c) {
      cl(f, c), r = !1;
    },
    d(c) {
      c && (oe(e), oe(s), oe(o)), f && f.d(c), a && a.d(), u && u.d(c);
    }
  };
}
function hl(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { show_label: s = !0 } = e, { show_legend: o = !0 } = e, { show_legend_label: r = !0 } = e, { legend_label: _ = "Highlights:" } = e, { _color_map: f = {} } = e, { info: a = void 0 } = e;
  return l.$$set = (u) => {
    "show_label" in u && t(0, s = u.show_label), "show_legend" in u && t(1, o = u.show_legend), "show_legend_label" in u && t(2, r = u.show_legend_label), "legend_label" in u && t(3, _ = u.legend_label), "_color_map" in u && t(4, f = u._color_map), "info" in u && t(5, a = u.info), "$$scope" in u && t(6, i = u.$$scope);
  }, [
    s,
    o,
    r,
    _,
    f,
    a,
    i,
    n
  ];
}
class bl extends nl {
  constructor(e) {
    super(), _l(this, e, hl, ml, rl, {
      show_label: 0,
      show_legend: 1,
      show_legend_label: 2,
      legend_label: 3,
      _color_map: 4,
      info: 5
    });
  }
}
const {
  SvelteComponent: gl,
  append: wl,
  attr: te,
  detach: kl,
  init: vl,
  insert: pl,
  noop: Ze,
  safe_not_equal: yl,
  svg_element: st
} = window.__gradio__svelte__internal;
function Cl(l) {
  let e, t;
  return {
    c() {
      e = st("svg"), t = st("polyline"), te(t, "points", "20 6 9 17 4 12"), te(e, "xmlns", "http://www.w3.org/2000/svg"), te(e, "viewBox", "2 0 20 20"), te(e, "fill", "none"), te(e, "stroke", "currentColor"), te(e, "stroke-width", "3"), te(e, "stroke-linecap", "round"), te(e, "stroke-linejoin", "round");
    },
    m(n, i) {
      pl(n, e, i), wl(e, t);
    },
    p: Ze,
    i: Ze,
    o: Ze,
    d(n) {
      n && kl(e);
    }
  };
}
class ql extends gl {
  constructor(e) {
    super(), vl(this, e, null, Cl, yl, {});
  }
}
const {
  SvelteComponent: Tl,
  append: ot,
  attr: re,
  detach: Ll,
  init: Sl,
  insert: Fl,
  noop: Oe,
  safe_not_equal: Hl,
  svg_element: Re
} = window.__gradio__svelte__internal;
function Ml(l) {
  let e, t, n;
  return {
    c() {
      e = Re("svg"), t = Re("path"), n = Re("path"), re(t, "fill", "currentColor"), re(t, "d", "M28 10v18H10V10h18m0-2H10a2 2 0 0 0-2 2v18a2 2 0 0 0 2 2h18a2 2 0 0 0 2-2V10a2 2 0 0 0-2-2Z"), re(n, "fill", "currentColor"), re(n, "d", "M4 18H2V4a2 2 0 0 1 2-2h14v2H4Z"), re(e, "xmlns", "http://www.w3.org/2000/svg"), re(e, "viewBox", "0 0 33 33"), re(e, "color", "currentColor");
    },
    m(i, s) {
      Fl(i, e, s), ot(e, t), ot(e, n);
    },
    p: Oe,
    i: Oe,
    o: Oe,
    d(i) {
      i && Ll(e);
    }
  };
}
class jl extends Tl {
  constructor(e) {
    super(), Sl(this, e, null, Ml, Hl, {});
  }
}
function Ae() {
}
const Nl = (l) => l;
function Vl(l, e) {
  return l != l ? e == e : l !== e || l && typeof l == "object" || typeof l == "function";
}
const Dt = typeof window < "u";
let ft = Dt ? () => window.performance.now() : () => Date.now(), It = Dt ? (l) => requestAnimationFrame(l) : Ae;
const qe = /* @__PURE__ */ new Set();
function Wt(l) {
  qe.forEach((e) => {
    e.c(l) || (qe.delete(e), e.f());
  }), qe.size !== 0 && It(Wt);
}
function zl(l) {
  let e;
  return qe.size === 0 && It(Wt), {
    promise: new Promise((t) => {
      qe.add(e = { c: l, f: t });
    }),
    abort() {
      qe.delete(e);
    }
  };
}
function Al(l, { delay: e = 0, duration: t = 400, easing: n = Nl } = {}) {
  const i = +getComputedStyle(l).opacity;
  return {
    delay: e,
    duration: t,
    easing: n,
    css: (s) => `opacity: ${s * i}`
  };
}
const ve = [];
function Bl(l, e = Ae) {
  let t;
  const n = /* @__PURE__ */ new Set();
  function i(r) {
    if (Vl(l, r) && (l = r, t)) {
      const _ = !ve.length;
      for (const f of n)
        f[1](), ve.push(f, l);
      if (_) {
        for (let f = 0; f < ve.length; f += 2)
          ve[f][0](ve[f + 1]);
        ve.length = 0;
      }
    }
  }
  function s(r) {
    i(r(l));
  }
  function o(r, _ = Ae) {
    const f = [r, _];
    return n.add(f), n.size === 1 && (t = e(i, s) || Ae), r(l), () => {
      n.delete(f), n.size === 0 && t && (t(), t = null);
    };
  }
  return { set: i, update: s, subscribe: o };
}
function at(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function Ie(l, e, t, n) {
  if (typeof t == "number" || at(t)) {
    const i = n - t, s = (t - e) / (l.dt || 1 / 60), o = l.opts.stiffness * i, r = l.opts.damping * s, _ = (o - r) * l.inv_mass, f = (s + _) * l.dt;
    return Math.abs(f) < l.opts.precision && Math.abs(i) < l.opts.precision ? n : (l.settled = !1, at(t) ? new Date(t.getTime() + f) : t + f);
  } else {
    if (Array.isArray(t))
      return t.map(
        (i, s) => Ie(l, e[s], t[s], n[s])
      );
    if (typeof t == "object") {
      const i = {};
      for (const s in t)
        i[s] = Ie(l, e[s], t[s], n[s]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function _t(l, e = {}) {
  const t = Bl(l), { stiffness: n = 0.15, damping: i = 0.8, precision: s = 0.01 } = e;
  let o, r, _, f = l, a = l, u = 1, c = 0, m = !1;
  function y(T, L = {}) {
    a = T;
    const C = _ = {};
    return l == null || L.hard || S.stiffness >= 1 && S.damping >= 1 ? (m = !0, o = ft(), f = T, t.set(l = a), Promise.resolve()) : (L.soft && (c = 1 / ((L.soft === !0 ? 0.5 : +L.soft) * 60), u = 0), r || (o = ft(), m = !1, r = zl((d) => {
      if (m)
        return m = !1, r = null, !1;
      u = Math.min(u + c, 1);
      const p = {
        inv_mass: u,
        opts: S,
        settled: !0,
        dt: (d - o) * 60 / 1e3
      }, H = Ie(p, f, l, a);
      return o = d, f = l, t.set(l = H), p.settled && (r = null), !p.settled;
    })), new Promise((d) => {
      r.promise.then(() => {
        C === _ && d();
      });
    }));
  }
  const S = {
    set: y,
    update: (T, L) => y(T(a, l), L),
    subscribe: t.subscribe,
    stiffness: n,
    damping: i,
    precision: s
  };
  return S;
}
const rt = [
  "red",
  "green",
  "blue",
  "yellow",
  "purple",
  "teal",
  "orange",
  "cyan",
  "lime",
  "pink"
], El = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], ut = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
}, ct = El.reduce(
  (l, { color: e, primary: t, secondary: n }) => ({
    ...l,
    [e]: {
      primary: ut[e][t],
      secondary: ut[e][n]
    }
  }),
  {}
), Pl = (l) => rt[l % rt.length];
function dt(l, e, t) {
  if (!t) {
    var n = document.createElement("canvas");
    t = n.getContext("2d");
  }
  t.fillStyle = l, t.fillRect(0, 0, 1, 1);
  const [i, s, o] = t.getImageData(0, 0, 1, 1).data;
  return t.clearRect(0, 0, 1, 1), `rgba(${i}, ${s}, ${o}, ${255 / e})`;
}
function Zl(l, e, t) {
  var n = {};
  for (const i in l) {
    const s = l[i].trim();
    s in ct ? n[i] = ct[s] : n[i] = {
      primary: e ? dt(l[i], 1, t) : l[i],
      secondary: e ? dt(l[i], 0.5, t) : l[i]
    };
  }
  return n;
}
function Ol(l, e) {
  let t = [], n = null, i = null;
  for (const [s, o] of l)
    e === "empty" && o === null || e === "equal" && i === o ? n = n ? n + s : s : (n !== null && t.push([n, i]), n = s, i = o);
  return n !== null && t.push([n, i]), t;
}
function Rl(l) {
  const e = window.getSelection();
  if (e.rangeCount > 0) {
    const t = document.createRange();
    return t.setStart(l, 0), e.anchorNode !== null && t.setEnd(e.anchorNode, e.anchorOffset), t.toString().length;
  }
  return -1;
}
function Dl(l, e) {
  var t = document.createTreeWalker(l, NodeFilter.SHOW_TEXT), n = t.nextNode();
  if (!n || !n.textContent)
    return null;
  for (var i = n.textContent.length; i < e; )
    if (n = t.nextNode(), n && n.textContent)
      i += n.textContent.length;
    else
      return null;
  var s = n.textContent.length - (i - e);
  return { node: n, offset: s };
}
const {
  SvelteComponent: Il,
  add_render_callback: Ye,
  append: mt,
  attr: B,
  binding_callbacks: ht,
  bubble: pe,
  check_outros: Ut,
  create_component: Ge,
  create_in_transition: Wl,
  destroy_component: Je,
  detach: me,
  element: Me,
  empty: Ul,
  group_outros: Xt,
  init: Xl,
  insert: he,
  listen: G,
  mount_component: Ke,
  noop: Yt,
  run_all: Yl,
  safe_not_equal: Gl,
  set_data: Jl,
  space: bt,
  text: Kl,
  toggle_class: gt,
  transition_in: ne,
  transition_out: de
} = window.__gradio__svelte__internal, { beforeUpdate: Ql, afterUpdate: xl, createEventDispatcher: $l } = window.__gradio__svelte__internal;
function en(l) {
  let e;
  return {
    c() {
      e = Kl(
        /*label*/
        l[0]
      );
    },
    m(t, n) {
      he(t, e, n);
    },
    p(t, n) {
      n[0] & /*label*/
      1 && Jl(
        e,
        /*label*/
        t[0]
      );
    },
    d(t) {
      t && me(e);
    }
  };
}
function wt(l) {
  let e, t, n, i;
  const s = [ln, tn], o = [];
  function r(_, f) {
    return (
      /*copied*/
      _[13] ? 0 : 1
    );
  }
  return e = r(l), t = o[e] = s[e](l), {
    c() {
      t.c(), n = Ul();
    },
    m(_, f) {
      o[e].m(_, f), he(_, n, f), i = !0;
    },
    p(_, f) {
      let a = e;
      e = r(_), e === a ? o[e].p(_, f) : (Xt(), de(o[a], 1, 1, () => {
        o[a] = null;
      }), Ut(), t = o[e], t ? t.p(_, f) : (t = o[e] = s[e](_), t.c()), ne(t, 1), t.m(n.parentNode, n));
    },
    i(_) {
      i || (ne(t), i = !0);
    },
    o(_) {
      de(t), i = !1;
    },
    d(_) {
      _ && me(n), o[e].d(_);
    }
  };
}
function tn(l) {
  let e, t, n, i, s;
  return t = new jl({}), {
    c() {
      e = Me("button"), Ge(t.$$.fragment), B(e, "aria-label", "Copy"), B(e, "aria-roledescription", "Copy text"), B(e, "class", "svelte-14ssfqr");
    },
    m(o, r) {
      he(o, e, r), Ke(t, e, null), n = !0, i || (s = G(
        e,
        "click",
        /*handle_copy*/
        l[14]
      ), i = !0);
    },
    p: Yt,
    i(o) {
      n || (ne(t.$$.fragment, o), n = !0);
    },
    o(o) {
      de(t.$$.fragment, o), n = !1;
    },
    d(o) {
      o && me(e), Je(t), i = !1, s();
    }
  };
}
function ln(l) {
  let e, t, n, i;
  return t = new ql({}), {
    c() {
      e = Me("button"), Ge(t.$$.fragment), B(e, "aria-label", "Copied"), B(e, "aria-roledescription", "Text copied"), B(e, "class", "svelte-14ssfqr");
    },
    m(s, o) {
      he(s, e, o), Ke(t, e, null), i = !0;
    },
    p: Yt,
    i(s) {
      i || (ne(t.$$.fragment, s), s && (n || Ye(() => {
        n = Wl(e, Al, { duration: 300 }), n.start();
      })), i = !0);
    },
    o(s) {
      de(t.$$.fragment, s), i = !1;
    },
    d(s) {
      s && me(e), Je(t);
    }
  };
}
function nn(l) {
  let e, t, n;
  return {
    c() {
      e = Me("div"), B(e, "class", "textfield svelte-14ssfqr"), B(e, "data-testid", "highlighted-textbox"), B(e, "contenteditable", "true"), /*el_text*/
      (l[11] === void 0 || /*marked_el_text*/
      l[9] === void 0) && Ye(() => (
        /*div_input_handler_1*/
        l[28].call(e)
      ));
    },
    m(i, s) {
      he(i, e, s), l[27](e), /*el_text*/
      l[11] !== void 0 && (e.textContent = /*el_text*/
      l[11]), /*marked_el_text*/
      l[9] !== void 0 && (e.innerHTML = /*marked_el_text*/
      l[9]), t || (n = [
        G(
          e,
          "input",
          /*div_input_handler_1*/
          l[28]
        ),
        G(
          e,
          "blur",
          /*blur_handler*/
          l[19]
        ),
        G(
          e,
          "keypress",
          /*keypress_handler*/
          l[20]
        ),
        G(
          e,
          "select",
          /*select_handler*/
          l[21]
        ),
        G(
          e,
          "scroll",
          /*scroll_handler*/
          l[22]
        ),
        G(
          e,
          "input",
          /*input_handler*/
          l[23]
        ),
        G(
          e,
          "focus",
          /*focus_handler*/
          l[24]
        ),
        G(
          e,
          "change",
          /*checkAndRemoveHighlight*/
          l[15]
        )
      ], t = !0);
    },
    p(i, s) {
      s[0] & /*el_text*/
      2048 && /*el_text*/
      i[11] !== e.textContent && (e.textContent = /*el_text*/
      i[11]), s[0] & /*marked_el_text*/
      512 && /*marked_el_text*/
      i[9] !== e.innerHTML && (e.innerHTML = /*marked_el_text*/
      i[9]);
    },
    d(i) {
      i && me(e), l[27](null), t = !1, Yl(n);
    }
  };
}
function sn(l) {
  let e, t, n;
  return {
    c() {
      e = Me("div"), B(e, "class", "textfield svelte-14ssfqr"), B(e, "data-testid", "highlighted-textbox"), B(e, "contenteditable", "false"), /*el_text*/
      (l[11] === void 0 || /*marked_el_text*/
      l[9] === void 0) && Ye(() => (
        /*div_input_handler*/
        l[26].call(e)
      ));
    },
    m(i, s) {
      he(i, e, s), l[25](e), /*el_text*/
      l[11] !== void 0 && (e.textContent = /*el_text*/
      l[11]), /*marked_el_text*/
      l[9] !== void 0 && (e.innerHTML = /*marked_el_text*/
      l[9]), t || (n = G(
        e,
        "input",
        /*div_input_handler*/
        l[26]
      ), t = !0);
    },
    p(i, s) {
      s[0] & /*el_text*/
      2048 && /*el_text*/
      i[11] !== e.textContent && (e.textContent = /*el_text*/
      i[11]), s[0] & /*marked_el_text*/
      512 && /*marked_el_text*/
      i[9] !== e.innerHTML && (e.innerHTML = /*marked_el_text*/
      i[9]);
    },
    d(i) {
      i && me(e), l[25](null), t = !1, n();
    }
  };
}
function on(l) {
  let e, t, n, i, s;
  t = new bl({
    props: {
      show_label: (
        /*show_label*/
        l[3]
      ),
      show_legend: (
        /*show_legend*/
        l[4]
      ),
      show_legend_label: (
        /*show_legend_label*/
        l[5]
      ),
      legend_label: (
        /*legend_label*/
        l[1]
      ),
      _color_map: (
        /*_color_map*/
        l[12]
      ),
      info: (
        /*info*/
        l[2]
      ),
      $$slots: { default: [en] },
      $$scope: { ctx: l }
    }
  });
  let o = (
    /*show_copy_button*/
    l[7] && wt(l)
  );
  function r(a, u) {
    return (
      /*disabled*/
      a[8] ? sn : nn
    );
  }
  let _ = r(l), f = _(l);
  return {
    c() {
      e = Me("label"), Ge(t.$$.fragment), n = bt(), o && o.c(), i = bt(), f.c(), B(e, "class", "svelte-14ssfqr"), gt(
        e,
        "container",
        /*container*/
        l[6]
      );
    },
    m(a, u) {
      he(a, e, u), Ke(t, e, null), mt(e, n), o && o.m(e, null), mt(e, i), f.m(e, null), s = !0;
    },
    p(a, u) {
      const c = {};
      u[0] & /*show_label*/
      8 && (c.show_label = /*show_label*/
      a[3]), u[0] & /*show_legend*/
      16 && (c.show_legend = /*show_legend*/
      a[4]), u[0] & /*show_legend_label*/
      32 && (c.show_legend_label = /*show_legend_label*/
      a[5]), u[0] & /*legend_label*/
      2 && (c.legend_label = /*legend_label*/
      a[1]), u[0] & /*_color_map*/
      4096 && (c._color_map = /*_color_map*/
      a[12]), u[0] & /*info*/
      4 && (c.info = /*info*/
      a[2]), u[0] & /*label*/
      1 | u[1] & /*$$scope*/
      512 && (c.$$scope = { dirty: u, ctx: a }), t.$set(c), /*show_copy_button*/
      a[7] ? o ? (o.p(a, u), u[0] & /*show_copy_button*/
      128 && ne(o, 1)) : (o = wt(a), o.c(), ne(o, 1), o.m(e, i)) : o && (Xt(), de(o, 1, 1, () => {
        o = null;
      }), Ut()), _ === (_ = r(a)) && f ? f.p(a, u) : (f.d(1), f = _(a), f && (f.c(), f.m(e, null))), (!s || u[0] & /*container*/
      64) && gt(
        e,
        "container",
        /*container*/
        a[6]
      );
    },
    i(a) {
      s || (ne(t.$$.fragment, a), ne(o), s = !0);
    },
    o(a) {
      de(t.$$.fragment, a), de(o), s = !1;
    },
    d(a) {
      a && me(e), Je(t), o && o.d(), f.d();
    }
  };
}
function fn(l) {
  let e, t = l[0], n = 1;
  for (; n < l.length; ) {
    const i = l[n], s = l[n + 1];
    if (n += 2, (i === "optionalAccess" || i === "optionalCall") && t == null)
      return;
    i === "access" || i === "optionalAccess" ? (e = t, t = s(t)) : (i === "call" || i === "optionalCall") && (t = s((...o) => t.call(e, ...o)), e = void 0);
  }
  return t;
}
function an(l, e, t) {
  const n = typeof document < "u";
  let { value: i = [] } = e, { value_is_output: s = !1 } = e, { label: o } = e, { legend_label: r } = e, { info: _ = void 0 } = e, { show_label: f = !0 } = e, { show_legend: a = !1 } = e, { show_legend_label: u = !1 } = e, { container: c = !0 } = e, { color_map: m = {} } = e, { show_copy_button: y = !1 } = e, { disabled: S } = e, T, L = "", C = "", d, p = !m || Object.keys(m).length === 0 ? {} : m, H = {}, b = !1, R;
  function Q() {
    for (let h in p)
      i.map(([N, j]) => j).includes(h) || delete p[h];
    if (i.length > 0) {
      for (let [h, N] of i)
        if (N !== null && !(N in p)) {
          let j = Pl(Object.keys(p).length);
          p[N] = j;
        }
    }
    t(12, H = Zl(p, n, d));
  }
  function E(h) {
    i.length > 0 && h && (t(11, L = i.map(([N, j]) => N).join(" ")), t(9, C = i.map(([N, j]) => j !== null ? `<mark class="hl ${j}" style="background-color:${H[j].secondary}">${N}</mark>` : N).join(" ") + " "));
  }
  const P = $l();
  Ql(() => {
    T && T.offsetHeight + T.scrollTop > T.scrollHeight - 100;
  });
  function X() {
    P("change", C), s || P("input"), z();
  }
  xl(() => {
    Q(), E(s), t(17, s = !1);
  });
  function be() {
    let h = [], N = "", j = null, ee = !1, ke = "";
    for (let ae = 0; ae < C.length; ae++) {
      let _e = C[ae];
      _e === "<" ? (ee = !0, N && h.push([N, j]), N = "", j = null) : _e === ">" ? (ee = !1, ke.startsWith("mark") && (j = fn([
        ke,
        "access",
        (Y) => Y.match,
        "call",
        (Y) => Y(/class="hl ([^"]+)"/),
        "optionalAccess",
        (Y) => Y[1]
      ]) || null), ke = "") : ee ? ke += _e : N += _e;
    }
    N && h.push([N, j]), t(16, i = h);
  }
  async function D() {
    "clipboard" in navigator && (await navigator.clipboard.writeText(L), x());
  }
  function x() {
    t(13, b = !0), R && clearTimeout(R), R = setTimeout(
      () => {
        t(13, b = !1);
      },
      1e3
    );
  }
  function z() {
    const h = window.getSelection(), N = h.anchorOffset;
    if (h.rangeCount > 0) {
      var j = h.getRangeAt(0).commonAncestorContainer.parentElement;
      if (j && j.tagName.toLowerCase() === "mark") {
        const tl = j.textContent;
        var ee = j.parentElement, ke = document.createTextNode(tl);
        ee.replaceChild(ke, j), t(9, C = ee.innerHTML);
        var ae = document.createRange(), _e = window.getSelection();
        const ll = N + Rl(ee);
        var Y = Dl(ee, ll);
        ae.setStart(Y.node, Y.offset), ae.setEnd(Y.node, Y.offset), _e.removeAllRanges(), _e.addRange(ae);
      }
    }
    be(), P("change", C);
  }
  function ge(h) {
    pe.call(this, l, h);
  }
  function g(h) {
    pe.call(this, l, h);
  }
  function je(h) {
    pe.call(this, l, h);
  }
  function Ne(h) {
    pe.call(this, l, h);
  }
  function we(h) {
    pe.call(this, l, h);
  }
  function Ee(h) {
    pe.call(this, l, h);
  }
  function Pe(h) {
    ht[h ? "unshift" : "push"](() => {
      T = h, t(10, T);
    });
  }
  function w() {
    L = this.textContent, C = this.innerHTML, t(11, L), t(9, C);
  }
  function $t(h) {
    ht[h ? "unshift" : "push"](() => {
      T = h, t(10, T);
    });
  }
  function el() {
    L = this.textContent, C = this.innerHTML, t(11, L), t(9, C);
  }
  return l.$$set = (h) => {
    "value" in h && t(16, i = h.value), "value_is_output" in h && t(17, s = h.value_is_output), "label" in h && t(0, o = h.label), "legend_label" in h && t(1, r = h.legend_label), "info" in h && t(2, _ = h.info), "show_label" in h && t(3, f = h.show_label), "show_legend" in h && t(4, a = h.show_legend), "show_legend_label" in h && t(5, u = h.show_legend_label), "container" in h && t(6, c = h.container), "color_map" in h && t(18, m = h.color_map), "show_copy_button" in h && t(7, y = h.show_copy_button), "disabled" in h && t(8, S = h.disabled);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*marked_el_text*/
    512 && X();
  }, Q(), E(!0), [
    o,
    r,
    _,
    f,
    a,
    u,
    c,
    y,
    S,
    C,
    T,
    L,
    H,
    b,
    D,
    z,
    i,
    s,
    m,
    ge,
    g,
    je,
    Ne,
    we,
    Ee,
    Pe,
    w,
    $t,
    el
  ];
}
class _n extends Il {
  constructor(e) {
    super(), Xl(
      this,
      e,
      an,
      on,
      Gl,
      {
        value: 16,
        value_is_output: 17,
        label: 0,
        legend_label: 1,
        info: 2,
        show_label: 3,
        show_legend: 4,
        show_legend_label: 5,
        container: 6,
        color_map: 18,
        show_copy_button: 7,
        disabled: 8
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: rn,
  assign: un,
  create_slot: cn,
  detach: dn,
  element: mn,
  get_all_dirty_from_scope: hn,
  get_slot_changes: bn,
  get_spread_update: gn,
  init: wn,
  insert: kn,
  safe_not_equal: vn,
  set_dynamic_element_data: kt,
  set_style: A,
  toggle_class: le,
  transition_in: Gt,
  transition_out: Jt,
  update_slot_base: pn
} = window.__gradio__svelte__internal;
function yn(l) {
  let e, t, n;
  const i = (
    /*#slots*/
    l[18].default
  ), s = cn(
    i,
    l,
    /*$$scope*/
    l[17],
    null
  );
  let o = [
    { "data-testid": (
      /*test_id*/
      l[7]
    ) },
    { id: (
      /*elem_id*/
      l[2]
    ) },
    {
      class: t = "block " + /*elem_classes*/
      l[3].join(" ") + " svelte-1t38q2d"
    }
  ], r = {};
  for (let _ = 0; _ < o.length; _ += 1)
    r = un(r, o[_]);
  return {
    c() {
      e = mn(
        /*tag*/
        l[14]
      ), s && s.c(), kt(
        /*tag*/
        l[14]
      )(e, r), le(
        e,
        "hidden",
        /*visible*/
        l[10] === !1
      ), le(
        e,
        "padded",
        /*padding*/
        l[6]
      ), le(
        e,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), le(e, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), A(
        e,
        "height",
        /*get_dimension*/
        l[15](
          /*height*/
          l[0]
        )
      ), A(e, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : (
        /*get_dimension*/
        l[15](
          /*width*/
          l[1]
        )
      )), A(
        e,
        "border-style",
        /*variant*/
        l[4]
      ), A(
        e,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), A(
        e,
        "flex-grow",
        /*scale*/
        l[12]
      ), A(e, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`), A(e, "border-width", "var(--block-border-width)");
    },
    m(_, f) {
      kn(_, e, f), s && s.m(e, null), n = !0;
    },
    p(_, f) {
      s && s.p && (!n || f & /*$$scope*/
      131072) && pn(
        s,
        i,
        _,
        /*$$scope*/
        _[17],
        n ? bn(
          i,
          /*$$scope*/
          _[17],
          f,
          null
        ) : hn(
          /*$$scope*/
          _[17]
        ),
        null
      ), kt(
        /*tag*/
        _[14]
      )(e, r = gn(o, [
        (!n || f & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          _[7]
        ) },
        (!n || f & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          _[2]
        ) },
        (!n || f & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        _[3].join(" ") + " svelte-1t38q2d")) && { class: t }
      ])), le(
        e,
        "hidden",
        /*visible*/
        _[10] === !1
      ), le(
        e,
        "padded",
        /*padding*/
        _[6]
      ), le(
        e,
        "border_focus",
        /*border_mode*/
        _[5] === "focus"
      ), le(e, "hide-container", !/*explicit_call*/
      _[8] && !/*container*/
      _[9]), f & /*height*/
      1 && A(
        e,
        "height",
        /*get_dimension*/
        _[15](
          /*height*/
          _[0]
        )
      ), f & /*width*/
      2 && A(e, "width", typeof /*width*/
      _[1] == "number" ? `calc(min(${/*width*/
      _[1]}px, 100%))` : (
        /*get_dimension*/
        _[15](
          /*width*/
          _[1]
        )
      )), f & /*variant*/
      16 && A(
        e,
        "border-style",
        /*variant*/
        _[4]
      ), f & /*allow_overflow*/
      2048 && A(
        e,
        "overflow",
        /*allow_overflow*/
        _[11] ? "visible" : "hidden"
      ), f & /*scale*/
      4096 && A(
        e,
        "flex-grow",
        /*scale*/
        _[12]
      ), f & /*min_width*/
      8192 && A(e, "min-width", `calc(min(${/*min_width*/
      _[13]}px, 100%))`);
    },
    i(_) {
      n || (Gt(s, _), n = !0);
    },
    o(_) {
      Jt(s, _), n = !1;
    },
    d(_) {
      _ && dn(e), s && s.d(_);
    }
  };
}
function Cn(l) {
  let e, t = (
    /*tag*/
    l[14] && yn(l)
  );
  return {
    c() {
      t && t.c();
    },
    m(n, i) {
      t && t.m(n, i), e = !0;
    },
    p(n, [i]) {
      /*tag*/
      n[14] && t.p(n, i);
    },
    i(n) {
      e || (Gt(t, n), e = !0);
    },
    o(n) {
      Jt(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function qn(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { height: s = void 0 } = e, { width: o = void 0 } = e, { elem_id: r = "" } = e, { elem_classes: _ = [] } = e, { variant: f = "solid" } = e, { border_mode: a = "base" } = e, { padding: u = !0 } = e, { type: c = "normal" } = e, { test_id: m = void 0 } = e, { explicit_call: y = !1 } = e, { container: S = !0 } = e, { visible: T = !0 } = e, { allow_overflow: L = !0 } = e, { scale: C = null } = e, { min_width: d = 0 } = e, p = c === "fieldset" ? "fieldset" : "div";
  const H = (b) => {
    if (b !== void 0) {
      if (typeof b == "number")
        return b + "px";
      if (typeof b == "string")
        return b;
    }
  };
  return l.$$set = (b) => {
    "height" in b && t(0, s = b.height), "width" in b && t(1, o = b.width), "elem_id" in b && t(2, r = b.elem_id), "elem_classes" in b && t(3, _ = b.elem_classes), "variant" in b && t(4, f = b.variant), "border_mode" in b && t(5, a = b.border_mode), "padding" in b && t(6, u = b.padding), "type" in b && t(16, c = b.type), "test_id" in b && t(7, m = b.test_id), "explicit_call" in b && t(8, y = b.explicit_call), "container" in b && t(9, S = b.container), "visible" in b && t(10, T = b.visible), "allow_overflow" in b && t(11, L = b.allow_overflow), "scale" in b && t(12, C = b.scale), "min_width" in b && t(13, d = b.min_width), "$$scope" in b && t(17, i = b.$$scope);
  }, [
    s,
    o,
    r,
    _,
    f,
    a,
    u,
    m,
    y,
    S,
    T,
    L,
    C,
    d,
    p,
    H,
    c,
    i,
    n
  ];
}
class Tn extends rn {
  constructor(e) {
    super(), wn(this, e, qn, Cn, vn, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 16,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
function ye(l) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; l > 1e3 && t < e.length - 1; )
    l /= 1e3, t++;
  let n = e[t];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
const {
  SvelteComponent: Ln,
  append: I,
  attr: q,
  component_subscribe: vt,
  detach: Sn,
  element: Fn,
  init: Hn,
  insert: Mn,
  noop: pt,
  safe_not_equal: jn,
  set_style: Ve,
  svg_element: W,
  toggle_class: yt
} = window.__gradio__svelte__internal, { onMount: Nn } = window.__gradio__svelte__internal;
function Vn(l) {
  let e, t, n, i, s, o, r, _, f, a, u, c;
  return {
    c() {
      e = Fn("div"), t = W("svg"), n = W("g"), i = W("path"), s = W("path"), o = W("path"), r = W("path"), _ = W("g"), f = W("path"), a = W("path"), u = W("path"), c = W("path"), q(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), q(i, "fill", "#FF7C00"), q(i, "fill-opacity", "0.4"), q(i, "class", "svelte-43sxxs"), q(s, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), q(s, "fill", "#FF7C00"), q(s, "class", "svelte-43sxxs"), q(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), q(o, "fill", "#FF7C00"), q(o, "fill-opacity", "0.4"), q(o, "class", "svelte-43sxxs"), q(r, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), q(r, "fill", "#FF7C00"), q(r, "class", "svelte-43sxxs"), Ve(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), q(f, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), q(f, "fill", "#FF7C00"), q(f, "fill-opacity", "0.4"), q(f, "class", "svelte-43sxxs"), q(a, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), q(a, "fill", "#FF7C00"), q(a, "class", "svelte-43sxxs"), q(u, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), q(u, "fill", "#FF7C00"), q(u, "fill-opacity", "0.4"), q(u, "class", "svelte-43sxxs"), q(c, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), q(c, "fill", "#FF7C00"), q(c, "class", "svelte-43sxxs"), Ve(_, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), q(t, "viewBox", "-1200 -1200 3000 3000"), q(t, "fill", "none"), q(t, "xmlns", "http://www.w3.org/2000/svg"), q(t, "class", "svelte-43sxxs"), q(e, "class", "svelte-43sxxs"), yt(
        e,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(m, y) {
      Mn(m, e, y), I(e, t), I(t, n), I(n, i), I(n, s), I(n, o), I(n, r), I(t, _), I(_, f), I(_, a), I(_, u), I(_, c);
    },
    p(m, [y]) {
      y & /*$top*/
      2 && Ve(n, "transform", "translate(" + /*$top*/
      m[1][0] + "px, " + /*$top*/
      m[1][1] + "px)"), y & /*$bottom*/
      4 && Ve(_, "transform", "translate(" + /*$bottom*/
      m[2][0] + "px, " + /*$bottom*/
      m[2][1] + "px)"), y & /*margin*/
      1 && yt(
        e,
        "margin",
        /*margin*/
        m[0]
      );
    },
    i: pt,
    o: pt,
    d(m) {
      m && Sn(e);
    }
  };
}
function zn(l, e, t) {
  let n, i, { margin: s = !0 } = e;
  const o = _t([0, 0]);
  vt(l, o, (c) => t(1, n = c));
  const r = _t([0, 0]);
  vt(l, r, (c) => t(2, i = c));
  let _;
  async function f() {
    await Promise.all([o.set([125, 140]), r.set([-125, -140])]), await Promise.all([o.set([-125, 140]), r.set([125, -140])]), await Promise.all([o.set([-125, 0]), r.set([125, -0])]), await Promise.all([o.set([125, 0]), r.set([-125, 0])]);
  }
  async function a() {
    await f(), _ || a();
  }
  async function u() {
    await Promise.all([o.set([125, 0]), r.set([-125, 0])]), a();
  }
  return Nn(() => (u(), () => _ = !0)), l.$$set = (c) => {
    "margin" in c && t(0, s = c.margin);
  }, [s, n, i, o, r];
}
class An extends Ln {
  constructor(e) {
    super(), Hn(this, e, zn, Vn, jn, { margin: 0 });
  }
}
const {
  SvelteComponent: Bn,
  append: ue,
  attr: J,
  binding_callbacks: Ct,
  check_outros: Kt,
  create_component: En,
  create_slot: Pn,
  destroy_component: Zn,
  destroy_each: Qt,
  detach: k,
  element: $,
  empty: Se,
  ensure_array_like: Be,
  get_all_dirty_from_scope: On,
  get_slot_changes: Rn,
  group_outros: xt,
  init: Dn,
  insert: v,
  mount_component: In,
  noop: We,
  safe_not_equal: Wn,
  set_data: O,
  set_style: ie,
  space: K,
  text: F,
  toggle_class: Z,
  transition_in: Te,
  transition_out: Le,
  update_slot_base: Un
} = window.__gradio__svelte__internal, { tick: Xn } = window.__gradio__svelte__internal, { onDestroy: Yn } = window.__gradio__svelte__internal, Gn = (l) => ({}), qt = (l) => ({});
function Tt(l, e, t) {
  const n = l.slice();
  return n[38] = e[t], n[40] = t, n;
}
function Lt(l, e, t) {
  const n = l.slice();
  return n[38] = e[t], n;
}
function Jn(l) {
  let e, t = (
    /*i18n*/
    l[1]("common.error") + ""
  ), n, i, s;
  const o = (
    /*#slots*/
    l[29].error
  ), r = Pn(
    o,
    l,
    /*$$scope*/
    l[28],
    qt
  );
  return {
    c() {
      e = $("span"), n = F(t), i = K(), r && r.c(), J(e, "class", "error svelte-1txqlrd");
    },
    m(_, f) {
      v(_, e, f), ue(e, n), v(_, i, f), r && r.m(_, f), s = !0;
    },
    p(_, f) {
      (!s || f[0] & /*i18n*/
      2) && t !== (t = /*i18n*/
      _[1]("common.error") + "") && O(n, t), r && r.p && (!s || f[0] & /*$$scope*/
      268435456) && Un(
        r,
        o,
        _,
        /*$$scope*/
        _[28],
        s ? Rn(
          o,
          /*$$scope*/
          _[28],
          f,
          Gn
        ) : On(
          /*$$scope*/
          _[28]
        ),
        qt
      );
    },
    i(_) {
      s || (Te(r, _), s = !0);
    },
    o(_) {
      Le(r, _), s = !1;
    },
    d(_) {
      _ && (k(e), k(i)), r && r.d(_);
    }
  };
}
function Kn(l) {
  let e, t, n, i, s, o, r, _, f, a = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && St(l)
  );
  function u(d, p) {
    if (
      /*progress*/
      d[7]
    )
      return $n;
    if (
      /*queue_position*/
      d[2] !== null && /*queue_size*/
      d[3] !== void 0 && /*queue_position*/
      d[2] >= 0
    )
      return xn;
    if (
      /*queue_position*/
      d[2] === 0
    )
      return Qn;
  }
  let c = u(l), m = c && c(l), y = (
    /*timer*/
    l[5] && Mt(l)
  );
  const S = [ni, li], T = [];
  function L(d, p) {
    return (
      /*last_progress_level*/
      d[15] != null ? 0 : (
        /*show_progress*/
        d[6] === "full" ? 1 : -1
      )
    );
  }
  ~(s = L(l)) && (o = T[s] = S[s](l));
  let C = !/*timer*/
  l[5] && Et(l);
  return {
    c() {
      a && a.c(), e = K(), t = $("div"), m && m.c(), n = K(), y && y.c(), i = K(), o && o.c(), r = K(), C && C.c(), _ = Se(), J(t, "class", "progress-text svelte-1txqlrd"), Z(
        t,
        "meta-text-center",
        /*variant*/
        l[8] === "center"
      ), Z(
        t,
        "meta-text",
        /*variant*/
        l[8] === "default"
      );
    },
    m(d, p) {
      a && a.m(d, p), v(d, e, p), v(d, t, p), m && m.m(t, null), ue(t, n), y && y.m(t, null), v(d, i, p), ~s && T[s].m(d, p), v(d, r, p), C && C.m(d, p), v(d, _, p), f = !0;
    },
    p(d, p) {
      /*variant*/
      d[8] === "default" && /*show_eta_bar*/
      d[18] && /*show_progress*/
      d[6] === "full" ? a ? a.p(d, p) : (a = St(d), a.c(), a.m(e.parentNode, e)) : a && (a.d(1), a = null), c === (c = u(d)) && m ? m.p(d, p) : (m && m.d(1), m = c && c(d), m && (m.c(), m.m(t, n))), /*timer*/
      d[5] ? y ? y.p(d, p) : (y = Mt(d), y.c(), y.m(t, null)) : y && (y.d(1), y = null), (!f || p[0] & /*variant*/
      256) && Z(
        t,
        "meta-text-center",
        /*variant*/
        d[8] === "center"
      ), (!f || p[0] & /*variant*/
      256) && Z(
        t,
        "meta-text",
        /*variant*/
        d[8] === "default"
      );
      let H = s;
      s = L(d), s === H ? ~s && T[s].p(d, p) : (o && (xt(), Le(T[H], 1, 1, () => {
        T[H] = null;
      }), Kt()), ~s ? (o = T[s], o ? o.p(d, p) : (o = T[s] = S[s](d), o.c()), Te(o, 1), o.m(r.parentNode, r)) : o = null), /*timer*/
      d[5] ? C && (C.d(1), C = null) : C ? C.p(d, p) : (C = Et(d), C.c(), C.m(_.parentNode, _));
    },
    i(d) {
      f || (Te(o), f = !0);
    },
    o(d) {
      Le(o), f = !1;
    },
    d(d) {
      d && (k(e), k(t), k(i), k(r), k(_)), a && a.d(d), m && m.d(), y && y.d(), ~s && T[s].d(d), C && C.d(d);
    }
  };
}
function St(l) {
  let e, t = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = $("div"), J(e, "class", "eta-bar svelte-1txqlrd"), ie(e, "transform", t);
    },
    m(n, i) {
      v(n, e, i);
    },
    p(n, i) {
      i[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && ie(e, "transform", t);
    },
    d(n) {
      n && k(e);
    }
  };
}
function Qn(l) {
  let e;
  return {
    c() {
      e = F("processing |");
    },
    m(t, n) {
      v(t, e, n);
    },
    p: We,
    d(t) {
      t && k(e);
    }
  };
}
function xn(l) {
  let e, t = (
    /*queue_position*/
    l[2] + 1 + ""
  ), n, i, s, o;
  return {
    c() {
      e = F("queue: "), n = F(t), i = F("/"), s = F(
        /*queue_size*/
        l[3]
      ), o = F(" |");
    },
    m(r, _) {
      v(r, e, _), v(r, n, _), v(r, i, _), v(r, s, _), v(r, o, _);
    },
    p(r, _) {
      _[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      r[2] + 1 + "") && O(n, t), _[0] & /*queue_size*/
      8 && O(
        s,
        /*queue_size*/
        r[3]
      );
    },
    d(r) {
      r && (k(e), k(n), k(i), k(s), k(o));
    }
  };
}
function $n(l) {
  let e, t = Be(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = Ht(Lt(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = Se();
    },
    m(i, s) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, s);
      v(i, e, s);
    },
    p(i, s) {
      if (s[0] & /*progress*/
      128) {
        t = Be(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const r = Lt(i, t, o);
          n[o] ? n[o].p(r, s) : (n[o] = Ht(r), n[o].c(), n[o].m(e.parentNode, e));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && k(e), Qt(n, i);
    }
  };
}
function Ft(l) {
  let e, t = (
    /*p*/
    l[38].unit + ""
  ), n, i, s = " ", o;
  function r(a, u) {
    return (
      /*p*/
      a[38].length != null ? ti : ei
    );
  }
  let _ = r(l), f = _(l);
  return {
    c() {
      f.c(), e = K(), n = F(t), i = F(" | "), o = F(s);
    },
    m(a, u) {
      f.m(a, u), v(a, e, u), v(a, n, u), v(a, i, u), v(a, o, u);
    },
    p(a, u) {
      _ === (_ = r(a)) && f ? f.p(a, u) : (f.d(1), f = _(a), f && (f.c(), f.m(e.parentNode, e))), u[0] & /*progress*/
      128 && t !== (t = /*p*/
      a[38].unit + "") && O(n, t);
    },
    d(a) {
      a && (k(e), k(n), k(i), k(o)), f.d(a);
    }
  };
}
function ei(l) {
  let e = ye(
    /*p*/
    l[38].index || 0
  ) + "", t;
  return {
    c() {
      t = F(e);
    },
    m(n, i) {
      v(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = ye(
        /*p*/
        n[38].index || 0
      ) + "") && O(t, e);
    },
    d(n) {
      n && k(t);
    }
  };
}
function ti(l) {
  let e = ye(
    /*p*/
    l[38].index || 0
  ) + "", t, n, i = ye(
    /*p*/
    l[38].length
  ) + "", s;
  return {
    c() {
      t = F(e), n = F("/"), s = F(i);
    },
    m(o, r) {
      v(o, t, r), v(o, n, r), v(o, s, r);
    },
    p(o, r) {
      r[0] & /*progress*/
      128 && e !== (e = ye(
        /*p*/
        o[38].index || 0
      ) + "") && O(t, e), r[0] & /*progress*/
      128 && i !== (i = ye(
        /*p*/
        o[38].length
      ) + "") && O(s, i);
    },
    d(o) {
      o && (k(t), k(n), k(s));
    }
  };
}
function Ht(l) {
  let e, t = (
    /*p*/
    l[38].index != null && Ft(l)
  );
  return {
    c() {
      t && t.c(), e = Se();
    },
    m(n, i) {
      t && t.m(n, i), v(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[38].index != null ? t ? t.p(n, i) : (t = Ft(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && k(e), t && t.d(n);
    }
  };
}
function Mt(l) {
  let e, t = (
    /*eta*/
    l[0] ? `/${/*formatted_eta*/
    l[19]}` : ""
  ), n, i;
  return {
    c() {
      e = F(
        /*formatted_timer*/
        l[20]
      ), n = F(t), i = F("s");
    },
    m(s, o) {
      v(s, e, o), v(s, n, o), v(s, i, o);
    },
    p(s, o) {
      o[0] & /*formatted_timer*/
      1048576 && O(
        e,
        /*formatted_timer*/
        s[20]
      ), o[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      s[0] ? `/${/*formatted_eta*/
      s[19]}` : "") && O(n, t);
    },
    d(s) {
      s && (k(e), k(n), k(i));
    }
  };
}
function li(l) {
  let e, t;
  return e = new An({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      En(e.$$.fragment);
    },
    m(n, i) {
      In(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i[0] & /*variant*/
      256 && (s.margin = /*variant*/
      n[8] === "default"), e.$set(s);
    },
    i(n) {
      t || (Te(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Le(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Zn(e, n);
    }
  };
}
function ni(l) {
  let e, t, n, i, s, o = `${/*last_progress_level*/
  l[15] * 100}%`, r = (
    /*progress*/
    l[7] != null && jt(l)
  );
  return {
    c() {
      e = $("div"), t = $("div"), r && r.c(), n = K(), i = $("div"), s = $("div"), J(t, "class", "progress-level-inner svelte-1txqlrd"), J(s, "class", "progress-bar svelte-1txqlrd"), ie(s, "width", o), J(i, "class", "progress-bar-wrap svelte-1txqlrd"), J(e, "class", "progress-level svelte-1txqlrd");
    },
    m(_, f) {
      v(_, e, f), ue(e, t), r && r.m(t, null), ue(e, n), ue(e, i), ue(i, s), l[30](s);
    },
    p(_, f) {
      /*progress*/
      _[7] != null ? r ? r.p(_, f) : (r = jt(_), r.c(), r.m(t, null)) : r && (r.d(1), r = null), f[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      _[15] * 100}%`) && ie(s, "width", o);
    },
    i: We,
    o: We,
    d(_) {
      _ && k(e), r && r.d(), l[30](null);
    }
  };
}
function jt(l) {
  let e, t = Be(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = Bt(Tt(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = Se();
    },
    m(i, s) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, s);
      v(i, e, s);
    },
    p(i, s) {
      if (s[0] & /*progress_level, progress*/
      16512) {
        t = Be(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const r = Tt(i, t, o);
          n[o] ? n[o].p(r, s) : (n[o] = Bt(r), n[o].c(), n[o].m(e.parentNode, e));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && k(e), Qt(n, i);
    }
  };
}
function Nt(l) {
  let e, t, n, i, s = (
    /*i*/
    l[40] !== 0 && ii()
  ), o = (
    /*p*/
    l[38].desc != null && Vt(l)
  ), r = (
    /*p*/
    l[38].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[40]
    ] != null && zt()
  ), _ = (
    /*progress_level*/
    l[14] != null && At(l)
  );
  return {
    c() {
      s && s.c(), e = K(), o && o.c(), t = K(), r && r.c(), n = K(), _ && _.c(), i = Se();
    },
    m(f, a) {
      s && s.m(f, a), v(f, e, a), o && o.m(f, a), v(f, t, a), r && r.m(f, a), v(f, n, a), _ && _.m(f, a), v(f, i, a);
    },
    p(f, a) {
      /*p*/
      f[38].desc != null ? o ? o.p(f, a) : (o = Vt(f), o.c(), o.m(t.parentNode, t)) : o && (o.d(1), o = null), /*p*/
      f[38].desc != null && /*progress_level*/
      f[14] && /*progress_level*/
      f[14][
        /*i*/
        f[40]
      ] != null ? r || (r = zt(), r.c(), r.m(n.parentNode, n)) : r && (r.d(1), r = null), /*progress_level*/
      f[14] != null ? _ ? _.p(f, a) : (_ = At(f), _.c(), _.m(i.parentNode, i)) : _ && (_.d(1), _ = null);
    },
    d(f) {
      f && (k(e), k(t), k(n), k(i)), s && s.d(f), o && o.d(f), r && r.d(f), _ && _.d(f);
    }
  };
}
function ii(l) {
  let e;
  return {
    c() {
      e = F(" /");
    },
    m(t, n) {
      v(t, e, n);
    },
    d(t) {
      t && k(e);
    }
  };
}
function Vt(l) {
  let e = (
    /*p*/
    l[38].desc + ""
  ), t;
  return {
    c() {
      t = F(e);
    },
    m(n, i) {
      v(n, t, i);
    },
    p(n, i) {
      i[0] & /*progress*/
      128 && e !== (e = /*p*/
      n[38].desc + "") && O(t, e);
    },
    d(n) {
      n && k(t);
    }
  };
}
function zt(l) {
  let e;
  return {
    c() {
      e = F("-");
    },
    m(t, n) {
      v(t, e, n);
    },
    d(t) {
      t && k(e);
    }
  };
}
function At(l) {
  let e = (100 * /*progress_level*/
  (l[14][
    /*i*/
    l[40]
  ] || 0)).toFixed(1) + "", t, n;
  return {
    c() {
      t = F(e), n = F("%");
    },
    m(i, s) {
      v(i, t, s), v(i, n, s);
    },
    p(i, s) {
      s[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[40]
      ] || 0)).toFixed(1) + "") && O(t, e);
    },
    d(i) {
      i && (k(t), k(n));
    }
  };
}
function Bt(l) {
  let e, t = (
    /*p*/
    (l[38].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[40]
    ] != null) && Nt(l)
  );
  return {
    c() {
      t && t.c(), e = Se();
    },
    m(n, i) {
      t && t.m(n, i), v(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[38].desc != null || /*progress_level*/
      n[14] && /*progress_level*/
      n[14][
        /*i*/
        n[40]
      ] != null ? t ? t.p(n, i) : (t = Nt(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && k(e), t && t.d(n);
    }
  };
}
function Et(l) {
  let e, t;
  return {
    c() {
      e = $("p"), t = F(
        /*loading_text*/
        l[9]
      ), J(e, "class", "loading svelte-1txqlrd");
    },
    m(n, i) {
      v(n, e, i), ue(e, t);
    },
    p(n, i) {
      i[0] & /*loading_text*/
      512 && O(
        t,
        /*loading_text*/
        n[9]
      );
    },
    d(n) {
      n && k(e);
    }
  };
}
function si(l) {
  let e, t, n, i, s;
  const o = [Kn, Jn], r = [];
  function _(f, a) {
    return (
      /*status*/
      f[4] === "pending" ? 0 : (
        /*status*/
        f[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = _(l)) && (n = r[t] = o[t](l)), {
    c() {
      e = $("div"), n && n.c(), J(e, "class", i = "wrap " + /*variant*/
      l[8] + " " + /*show_progress*/
      l[6] + " svelte-1txqlrd"), Z(e, "hide", !/*status*/
      l[4] || /*status*/
      l[4] === "complete" || /*show_progress*/
      l[6] === "hidden"), Z(
        e,
        "translucent",
        /*variant*/
        l[8] === "center" && /*status*/
        (l[4] === "pending" || /*status*/
        l[4] === "error") || /*translucent*/
        l[11] || /*show_progress*/
        l[6] === "minimal"
      ), Z(
        e,
        "generating",
        /*status*/
        l[4] === "generating"
      ), Z(
        e,
        "border",
        /*border*/
        l[12]
      ), ie(
        e,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), ie(
        e,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(f, a) {
      v(f, e, a), ~t && r[t].m(e, null), l[31](e), s = !0;
    },
    p(f, a) {
      let u = t;
      t = _(f), t === u ? ~t && r[t].p(f, a) : (n && (xt(), Le(r[u], 1, 1, () => {
        r[u] = null;
      }), Kt()), ~t ? (n = r[t], n ? n.p(f, a) : (n = r[t] = o[t](f), n.c()), Te(n, 1), n.m(e, null)) : n = null), (!s || a[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      f[8] + " " + /*show_progress*/
      f[6] + " svelte-1txqlrd")) && J(e, "class", i), (!s || a[0] & /*variant, show_progress, status, show_progress*/
      336) && Z(e, "hide", !/*status*/
      f[4] || /*status*/
      f[4] === "complete" || /*show_progress*/
      f[6] === "hidden"), (!s || a[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && Z(
        e,
        "translucent",
        /*variant*/
        f[8] === "center" && /*status*/
        (f[4] === "pending" || /*status*/
        f[4] === "error") || /*translucent*/
        f[11] || /*show_progress*/
        f[6] === "minimal"
      ), (!s || a[0] & /*variant, show_progress, status*/
      336) && Z(
        e,
        "generating",
        /*status*/
        f[4] === "generating"
      ), (!s || a[0] & /*variant, show_progress, border*/
      4416) && Z(
        e,
        "border",
        /*border*/
        f[12]
      ), a[0] & /*absolute*/
      1024 && ie(
        e,
        "position",
        /*absolute*/
        f[10] ? "absolute" : "static"
      ), a[0] & /*absolute*/
      1024 && ie(
        e,
        "padding",
        /*absolute*/
        f[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(f) {
      s || (Te(n), s = !0);
    },
    o(f) {
      Le(n), s = !1;
    },
    d(f) {
      f && k(e), ~t && r[t].d(), l[31](null);
    }
  };
}
let ze = [], De = !1;
async function oi(l, e = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && e !== !0)) {
    if (ze.push(l), !De)
      De = !0;
    else
      return;
    await Xn(), requestAnimationFrame(() => {
      let t = [0, 0];
      for (let n = 0; n < ze.length; n++) {
        const s = ze[n].getBoundingClientRect();
        (n === 0 || s.top + window.scrollY <= t[0]) && (t[0] = s.top + window.scrollY, t[1] = n);
      }
      window.scrollTo({ top: t[0] - 20, behavior: "smooth" }), De = !1, ze = [];
    });
  }
}
function fi(l, e, t) {
  let n, { $$slots: i = {}, $$scope: s } = e, { i18n: o } = e, { eta: r = null } = e, { queue_position: _ } = e, { queue_size: f } = e, { status: a } = e, { scroll_to_output: u = !1 } = e, { timer: c = !0 } = e, { show_progress: m = "full" } = e, { message: y = null } = e, { progress: S = null } = e, { variant: T = "default" } = e, { loading_text: L = "Loading..." } = e, { absolute: C = !0 } = e, { translucent: d = !1 } = e, { border: p = !1 } = e, { autoscroll: H } = e, b, R = !1, Q = 0, E = 0, P = null, X = null, be = 0, D = null, x, z = null, ge = !0;
  const g = () => {
    t(0, r = t(26, P = t(19, we = null))), t(24, Q = performance.now()), t(25, E = 0), R = !0, je();
  };
  function je() {
    requestAnimationFrame(() => {
      t(25, E = (performance.now() - Q) / 1e3), R && je();
    });
  }
  function Ne() {
    t(25, E = 0), t(0, r = t(26, P = t(19, we = null))), R && (R = !1);
  }
  Yn(() => {
    R && Ne();
  });
  let we = null;
  function Ee(w) {
    Ct[w ? "unshift" : "push"](() => {
      z = w, t(16, z), t(7, S), t(14, D), t(15, x);
    });
  }
  function Pe(w) {
    Ct[w ? "unshift" : "push"](() => {
      b = w, t(13, b);
    });
  }
  return l.$$set = (w) => {
    "i18n" in w && t(1, o = w.i18n), "eta" in w && t(0, r = w.eta), "queue_position" in w && t(2, _ = w.queue_position), "queue_size" in w && t(3, f = w.queue_size), "status" in w && t(4, a = w.status), "scroll_to_output" in w && t(21, u = w.scroll_to_output), "timer" in w && t(5, c = w.timer), "show_progress" in w && t(6, m = w.show_progress), "message" in w && t(22, y = w.message), "progress" in w && t(7, S = w.progress), "variant" in w && t(8, T = w.variant), "loading_text" in w && t(9, L = w.loading_text), "absolute" in w && t(10, C = w.absolute), "translucent" in w && t(11, d = w.translucent), "border" in w && t(12, p = w.border), "autoscroll" in w && t(23, H = w.autoscroll), "$$scope" in w && t(28, s = w.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    218103809 && (r === null && t(0, r = P), r != null && P !== r && (t(27, X = (performance.now() - Q) / 1e3 + r), t(19, we = X.toFixed(1)), t(26, P = r))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    167772160 && t(17, be = X === null || X <= 0 || !E ? null : Math.min(E / X, 1)), l.$$.dirty[0] & /*progress*/
    128 && S != null && t(18, ge = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (S != null ? t(14, D = S.map((w) => {
      if (w.index != null && w.length != null)
        return w.index / w.length;
      if (w.progress != null)
        return w.progress;
    })) : t(14, D = null), D ? (t(15, x = D[D.length - 1]), z && (x === 0 ? t(16, z.style.transition = "0", z) : t(16, z.style.transition = "150ms", z))) : t(15, x = void 0)), l.$$.dirty[0] & /*status*/
    16 && (a === "pending" ? g() : Ne()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    10493968 && b && u && (a === "pending" || a === "complete") && oi(b, H), l.$$.dirty[0] & /*status, message*/
    4194320, l.$$.dirty[0] & /*timer_diff*/
    33554432 && t(20, n = E.toFixed(1));
  }, [
    r,
    o,
    _,
    f,
    a,
    c,
    m,
    S,
    T,
    L,
    C,
    d,
    p,
    b,
    D,
    x,
    z,
    be,
    ge,
    we,
    n,
    u,
    y,
    H,
    Q,
    E,
    P,
    X,
    s,
    i,
    Ee,
    Pe
  ];
}
class ai extends Bn {
  constructor(e) {
    super(), Dn(
      this,
      e,
      fi,
      si,
      Wn,
      {
        i18n: 1,
        eta: 0,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 21,
        timer: 5,
        show_progress: 6,
        message: 22,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 23
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: _i,
  add_flush_callback: Pt,
  assign: ri,
  bind: Zt,
  binding_callbacks: Ot,
  check_outros: ui,
  create_component: Qe,
  destroy_component: xe,
  detach: ci,
  flush: M,
  get_spread_object: di,
  get_spread_update: mi,
  group_outros: hi,
  init: bi,
  insert: gi,
  mount_component: $e,
  safe_not_equal: wi,
  space: ki,
  transition_in: Ce,
  transition_out: Fe
} = window.__gradio__svelte__internal;
function Rt(l) {
  let e, t;
  const n = [
    { autoscroll: (
      /*gradio*/
      l[3].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      l[3].i18n
    ) },
    /*loading_status*/
    l[17]
  ];
  let i = {};
  for (let s = 0; s < n.length; s += 1)
    i = ri(i, n[s]);
  return e = new ai({ props: i }), {
    c() {
      Qe(e.$$.fragment);
    },
    m(s, o) {
      $e(e, s, o), t = !0;
    },
    p(s, o) {
      const r = o & /*gradio, loading_status*/
      131080 ? mi(n, [
        o & /*gradio*/
        8 && { autoscroll: (
          /*gradio*/
          s[3].autoscroll
        ) },
        o & /*gradio*/
        8 && { i18n: (
          /*gradio*/
          s[3].i18n
        ) },
        o & /*loading_status*/
        131072 && di(
          /*loading_status*/
          s[17]
        )
      ]) : {};
      e.$set(r);
    },
    i(s) {
      t || (Ce(e.$$.fragment, s), t = !0);
    },
    o(s) {
      Fe(e.$$.fragment, s), t = !1;
    },
    d(s) {
      xe(e, s);
    }
  };
}
function vi(l) {
  let e, t, n, i, s, o = (
    /*loading_status*/
    l[17] && Rt(l)
  );
  function r(a) {
    l[22](a);
  }
  function _(a) {
    l[23](a);
  }
  let f = {
    label: (
      /*label*/
      l[4]
    ),
    info: (
      /*info*/
      l[6]
    ),
    show_label: (
      /*show_label*/
      l[10]
    ),
    show_legend: (
      /*show_legend*/
      l[11]
    ),
    show_legend_label: (
      /*show_legend_label*/
      l[12]
    ),
    legend_label: (
      /*legend_label*/
      l[5]
    ),
    color_map: (
      /*color_map*/
      l[1]
    ),
    show_copy_button: (
      /*show_copy_button*/
      l[16]
    ),
    container: (
      /*container*/
      l[13]
    ),
    disabled: !/*interactive*/
    l[18]
  };
  return (
    /*value*/
    l[0] !== void 0 && (f.value = /*value*/
    l[0]), /*value_is_output*/
    l[2] !== void 0 && (f.value_is_output = /*value_is_output*/
    l[2]), t = new _n({ props: f }), Ot.push(() => Zt(t, "value", r)), Ot.push(() => Zt(t, "value_is_output", _)), t.$on(
      "change",
      /*change_handler*/
      l[24]
    ), t.$on(
      "input",
      /*input_handler*/
      l[25]
    ), t.$on(
      "submit",
      /*submit_handler*/
      l[26]
    ), t.$on(
      "blur",
      /*blur_handler*/
      l[27]
    ), t.$on(
      "select",
      /*select_handler*/
      l[28]
    ), t.$on(
      "focus",
      /*focus_handler*/
      l[29]
    ), {
      c() {
        o && o.c(), e = ki(), Qe(t.$$.fragment);
      },
      m(a, u) {
        o && o.m(a, u), gi(a, e, u), $e(t, a, u), s = !0;
      },
      p(a, u) {
        /*loading_status*/
        a[17] ? o ? (o.p(a, u), u & /*loading_status*/
        131072 && Ce(o, 1)) : (o = Rt(a), o.c(), Ce(o, 1), o.m(e.parentNode, e)) : o && (hi(), Fe(o, 1, 1, () => {
          o = null;
        }), ui());
        const c = {};
        u & /*label*/
        16 && (c.label = /*label*/
        a[4]), u & /*info*/
        64 && (c.info = /*info*/
        a[6]), u & /*show_label*/
        1024 && (c.show_label = /*show_label*/
        a[10]), u & /*show_legend*/
        2048 && (c.show_legend = /*show_legend*/
        a[11]), u & /*show_legend_label*/
        4096 && (c.show_legend_label = /*show_legend_label*/
        a[12]), u & /*legend_label*/
        32 && (c.legend_label = /*legend_label*/
        a[5]), u & /*color_map*/
        2 && (c.color_map = /*color_map*/
        a[1]), u & /*show_copy_button*/
        65536 && (c.show_copy_button = /*show_copy_button*/
        a[16]), u & /*container*/
        8192 && (c.container = /*container*/
        a[13]), u & /*interactive*/
        262144 && (c.disabled = !/*interactive*/
        a[18]), !n && u & /*value*/
        1 && (n = !0, c.value = /*value*/
        a[0], Pt(() => n = !1)), !i && u & /*value_is_output*/
        4 && (i = !0, c.value_is_output = /*value_is_output*/
        a[2], Pt(() => i = !1)), t.$set(c);
      },
      i(a) {
        s || (Ce(o), Ce(t.$$.fragment, a), s = !0);
      },
      o(a) {
        Fe(o), Fe(t.$$.fragment, a), s = !1;
      },
      d(a) {
        a && ci(e), o && o.d(a), xe(t, a);
      }
    }
  );
}
function pi(l) {
  let e, t;
  return e = new Tn({
    props: {
      visible: (
        /*visible*/
        l[9]
      ),
      elem_id: (
        /*elem_id*/
        l[7]
      ),
      elem_classes: (
        /*elem_classes*/
        l[8]
      ),
      scale: (
        /*scale*/
        l[14]
      ),
      min_width: (
        /*min_width*/
        l[15]
      ),
      allow_overflow: !1,
      padding: (
        /*container*/
        l[13]
      ),
      $$slots: { default: [vi] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      Qe(e.$$.fragment);
    },
    m(n, i) {
      $e(e, n, i), t = !0;
    },
    p(n, [i]) {
      const s = {};
      i & /*visible*/
      512 && (s.visible = /*visible*/
      n[9]), i & /*elem_id*/
      128 && (s.elem_id = /*elem_id*/
      n[7]), i & /*elem_classes*/
      256 && (s.elem_classes = /*elem_classes*/
      n[8]), i & /*scale*/
      16384 && (s.scale = /*scale*/
      n[14]), i & /*min_width*/
      32768 && (s.min_width = /*min_width*/
      n[15]), i & /*container*/
      8192 && (s.padding = /*container*/
      n[13]), i & /*$$scope, label, info, show_label, show_legend, show_legend_label, legend_label, color_map, show_copy_button, container, interactive, value, value_is_output, gradio, loading_status*/
      1074216063 && (s.$$scope = { dirty: i, ctx: n }), e.$set(s);
    },
    i(n) {
      t || (Ce(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Fe(e.$$.fragment, n), t = !1;
    },
    d(n) {
      xe(e, n);
    }
  };
}
function yi(l, e, t) {
  let { gradio: n } = e, { label: i = "Highlighted Textbox" } = e, { legend_label: s = "Highlights:" } = e, { info: o = void 0 } = e, { elem_id: r = "" } = e, { elem_classes: _ = [] } = e, { visible: f = !0 } = e, { value: a } = e, { show_label: u } = e, { show_legend: c } = e, { show_legend_label: m } = e, { color_map: y = {} } = e, { container: S = !0 } = e, { scale: T = null } = e, { min_width: L = void 0 } = e, { show_copy_button: C = !1 } = e, { loading_status: d = void 0 } = e, { value_is_output: p = !1 } = e, { combine_adjacent: H = !1 } = e, { interactive: b = !0 } = e;
  const R = !1, Q = !0;
  function E(g) {
    a = g, t(0, a), t(19, H);
  }
  function P(g) {
    p = g, t(2, p);
  }
  const X = () => n.dispatch("change"), be = () => n.dispatch("input"), D = () => n.dispatch("submit"), x = () => n.dispatch("blur"), z = (g) => n.dispatch("select", g.detail), ge = () => n.dispatch("focus");
  return l.$$set = (g) => {
    "gradio" in g && t(3, n = g.gradio), "label" in g && t(4, i = g.label), "legend_label" in g && t(5, s = g.legend_label), "info" in g && t(6, o = g.info), "elem_id" in g && t(7, r = g.elem_id), "elem_classes" in g && t(8, _ = g.elem_classes), "visible" in g && t(9, f = g.visible), "value" in g && t(0, a = g.value), "show_label" in g && t(10, u = g.show_label), "show_legend" in g && t(11, c = g.show_legend), "show_legend_label" in g && t(12, m = g.show_legend_label), "color_map" in g && t(1, y = g.color_map), "container" in g && t(13, S = g.container), "scale" in g && t(14, T = g.scale), "min_width" in g && t(15, L = g.min_width), "show_copy_button" in g && t(16, C = g.show_copy_button), "loading_status" in g && t(17, d = g.loading_status), "value_is_output" in g && t(2, p = g.value_is_output), "combine_adjacent" in g && t(19, H = g.combine_adjacent), "interactive" in g && t(18, b = g.interactive);
  }, l.$$.update = () => {
    l.$$.dirty & /*color_map*/
    2 && !y && Object.keys(y).length && t(1, y), l.$$.dirty & /*value, combine_adjacent*/
    524289 && a && H && t(0, a = Ol(a, "equal"));
  }, [
    a,
    y,
    p,
    n,
    i,
    s,
    o,
    r,
    _,
    f,
    u,
    c,
    m,
    S,
    T,
    L,
    C,
    d,
    b,
    H,
    R,
    Q,
    E,
    P,
    X,
    be,
    D,
    x,
    z,
    ge
  ];
}
class Ci extends _i {
  constructor(e) {
    super(), bi(this, e, yi, pi, wi, {
      gradio: 3,
      label: 4,
      legend_label: 5,
      info: 6,
      elem_id: 7,
      elem_classes: 8,
      visible: 9,
      value: 0,
      show_label: 10,
      show_legend: 11,
      show_legend_label: 12,
      color_map: 1,
      container: 13,
      scale: 14,
      min_width: 15,
      show_copy_button: 16,
      loading_status: 17,
      value_is_output: 2,
      combine_adjacent: 19,
      interactive: 18,
      autofocus: 20,
      autoscroll: 21
    });
  }
  get gradio() {
    return this.$$.ctx[3];
  }
  set gradio(e) {
    this.$$set({ gradio: e }), M();
  }
  get label() {
    return this.$$.ctx[4];
  }
  set label(e) {
    this.$$set({ label: e }), M();
  }
  get legend_label() {
    return this.$$.ctx[5];
  }
  set legend_label(e) {
    this.$$set({ legend_label: e }), M();
  }
  get info() {
    return this.$$.ctx[6];
  }
  set info(e) {
    this.$$set({ info: e }), M();
  }
  get elem_id() {
    return this.$$.ctx[7];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), M();
  }
  get elem_classes() {
    return this.$$.ctx[8];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), M();
  }
  get visible() {
    return this.$$.ctx[9];
  }
  set visible(e) {
    this.$$set({ visible: e }), M();
  }
  get value() {
    return this.$$.ctx[0];
  }
  set value(e) {
    this.$$set({ value: e }), M();
  }
  get show_label() {
    return this.$$.ctx[10];
  }
  set show_label(e) {
    this.$$set({ show_label: e }), M();
  }
  get show_legend() {
    return this.$$.ctx[11];
  }
  set show_legend(e) {
    this.$$set({ show_legend: e }), M();
  }
  get show_legend_label() {
    return this.$$.ctx[12];
  }
  set show_legend_label(e) {
    this.$$set({ show_legend_label: e }), M();
  }
  get color_map() {
    return this.$$.ctx[1];
  }
  set color_map(e) {
    this.$$set({ color_map: e }), M();
  }
  get container() {
    return this.$$.ctx[13];
  }
  set container(e) {
    this.$$set({ container: e }), M();
  }
  get scale() {
    return this.$$.ctx[14];
  }
  set scale(e) {
    this.$$set({ scale: e }), M();
  }
  get min_width() {
    return this.$$.ctx[15];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), M();
  }
  get show_copy_button() {
    return this.$$.ctx[16];
  }
  set show_copy_button(e) {
    this.$$set({ show_copy_button: e }), M();
  }
  get loading_status() {
    return this.$$.ctx[17];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), M();
  }
  get value_is_output() {
    return this.$$.ctx[2];
  }
  set value_is_output(e) {
    this.$$set({ value_is_output: e }), M();
  }
  get combine_adjacent() {
    return this.$$.ctx[19];
  }
  set combine_adjacent(e) {
    this.$$set({ combine_adjacent: e }), M();
  }
  get interactive() {
    return this.$$.ctx[18];
  }
  set interactive(e) {
    this.$$set({ interactive: e }), M();
  }
  get autofocus() {
    return this.$$.ctx[20];
  }
  get autoscroll() {
    return this.$$.ctx[21];
  }
}
export {
  Ci as default
};
