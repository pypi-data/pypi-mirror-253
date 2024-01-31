const {
  SvelteComponent: ll,
  append: oe,
  attr: U,
  create_slot: nl,
  destroy_each: il,
  detach: fe,
  element: ue,
  empty: sl,
  ensure_array_like: tt,
  get_all_dirty_from_scope: ol,
  get_slot_changes: fl,
  init: _l,
  insert: _e,
  safe_not_equal: al,
  set_data: Xe,
  space: He,
  text: Ye,
  toggle_class: V,
  transition_in: rl,
  transition_out: ul,
  update_slot_base: cl
} = window.__gradio__svelte__internal;
function lt(l, e, t) {
  const n = l.slice();
  return n[8] = e[t][0], n[9] = e[t][1], n[11] = t, n;
}
function nt(l) {
  let e, t, n, i, s, o, r = tt(Object.entries(
    /*_color_map*/
    l[4]
  )), a = [];
  for (let f = 0; f < r.length; f += 1)
    a[f] = it(lt(l, r, f));
  return {
    c() {
      e = ue("span"), e.textContent = "·", t = He(), n = ue("div"), i = ue("span"), s = Ye(
        /*legend_label*/
        l[3]
      ), o = He();
      for (let f = 0; f < a.length; f += 1)
        a[f].c();
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
    m(f, _) {
      _e(f, e, _), _e(f, t, _), _e(f, n, _), oe(n, i), oe(i, s), oe(n, o);
      for (let u = 0; u < a.length; u += 1)
        a[u] && a[u].m(n, null);
    },
    p(f, _) {
      if (_ & /*show_legend, show_label*/
      3 && V(e, "hide", !/*show_legend*/
      f[1] || !/*show_label*/
      f[0]), _ & /*info*/
      32 && V(
        e,
        "has-info",
        /*info*/
        f[5] != null
      ), _ & /*legend_label*/
      8 && Xe(
        s,
        /*legend_label*/
        f[3]
      ), _ & /*show_legend_label*/
      4 && V(i, "hide", !/*show_legend_label*/
      f[2]), _ & /*info*/
      32 && V(
        i,
        "has-info",
        /*info*/
        f[5] != null
      ), _ & /*Object, _color_map, info*/
      48) {
        r = tt(Object.entries(
          /*_color_map*/
          f[4]
        ));
        let u;
        for (u = 0; u < r.length; u += 1) {
          const c = lt(f, r, u);
          a[u] ? a[u].p(c, _) : (a[u] = it(c), a[u].c(), a[u].m(n, null));
        }
        for (; u < a.length; u += 1)
          a[u].d(1);
        a.length = r.length;
      }
      _ & /*show_legend*/
      2 && V(n, "hide", !/*show_legend*/
      f[1]);
    },
    d(f) {
      f && (fe(e), fe(t), fe(n)), il(a, f);
    }
  };
}
function it(l) {
  let e, t = (
    /*category*/
    l[8] + ""
  ), n, i, s;
  return {
    c() {
      e = ue("div"), n = Ye(t), i = He(), U(e, "class", "category-label svelte-vm3q5z"), U(e, "style", s = "background-color:" + /*color*/
      l[9].secondary), V(
        e,
        "has-info",
        /*info*/
        l[5] != null
      );
    },
    m(o, r) {
      _e(o, e, r), oe(e, n), oe(e, i);
    },
    p(o, r) {
      r & /*_color_map*/
      16 && t !== (t = /*category*/
      o[8] + "") && Xe(n, t), r & /*_color_map*/
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
      o && fe(e);
    }
  };
}
function st(l) {
  let e, t;
  return {
    c() {
      e = ue("div"), t = Ye(
        /*info*/
        l[5]
      ), U(e, "class", "title-with-highlights-info svelte-vm3q5z");
    },
    m(n, i) {
      _e(n, e, i), oe(e, t);
    },
    p(n, i) {
      i & /*info*/
      32 && Xe(
        t,
        /*info*/
        n[5]
      );
    },
    d(n) {
      n && fe(e);
    }
  };
}
function dl(l) {
  let e, t, n, i = Object.keys(
    /*_color_map*/
    l[4]
  ).length !== 0, s, o, r;
  const a = (
    /*#slots*/
    l[7].default
  ), f = nl(
    a,
    l,
    /*$$scope*/
    l[6],
    null
  );
  let _ = i && nt(l), u = (
    /*info*/
    l[5] && st(l)
  );
  return {
    c() {
      e = ue("div"), t = ue("span"), f && f.c(), n = He(), _ && _.c(), s = He(), u && u.c(), o = sl(), U(t, "data-testid", "block-info"), U(t, "class", "svelte-vm3q5z"), V(t, "sr-only", !/*show_label*/
      l[0]), V(t, "hide", !/*show_label*/
      l[0]), V(
        t,
        "has-info",
        /*info*/
        l[5] != null
      ), U(e, "class", "title-container svelte-vm3q5z");
    },
    m(c, m) {
      _e(c, e, m), oe(e, t), f && f.m(t, null), oe(e, n), _ && _.m(e, null), _e(c, s, m), u && u.m(c, m), _e(c, o, m), r = !0;
    },
    p(c, [m]) {
      f && f.p && (!r || m & /*$$scope*/
      64) && cl(
        f,
        a,
        c,
        /*$$scope*/
        c[6],
        r ? fl(
          a,
          /*$$scope*/
          c[6],
          m,
          null
        ) : ol(
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
      ).length !== 0), i ? _ ? _.p(c, m) : (_ = nt(c), _.c(), _.m(e, null)) : _ && (_.d(1), _ = null), /*info*/
      c[5] ? u ? u.p(c, m) : (u = st(c), u.c(), u.m(o.parentNode, o)) : u && (u.d(1), u = null);
    },
    i(c) {
      r || (rl(f, c), r = !0);
    },
    o(c) {
      ul(f, c), r = !1;
    },
    d(c) {
      c && (fe(e), fe(s), fe(o)), f && f.d(c), _ && _.d(), u && u.d(c);
    }
  };
}
function ml(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { show_label: s = !0 } = e, { show_legend: o = !0 } = e, { show_legend_label: r = !0 } = e, { legend_label: a = "Highlights:" } = e, { _color_map: f = {} } = e, { info: _ = void 0 } = e;
  return l.$$set = (u) => {
    "show_label" in u && t(0, s = u.show_label), "show_legend" in u && t(1, o = u.show_legend), "show_legend_label" in u && t(2, r = u.show_legend_label), "legend_label" in u && t(3, a = u.legend_label), "_color_map" in u && t(4, f = u._color_map), "info" in u && t(5, _ = u.info), "$$scope" in u && t(6, i = u.$$scope);
  }, [
    s,
    o,
    r,
    a,
    f,
    _,
    i,
    n
  ];
}
class hl extends ll {
  constructor(e) {
    super(), _l(this, e, ml, dl, al, {
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
  SvelteComponent: bl,
  append: gl,
  attr: le,
  detach: wl,
  init: kl,
  insert: vl,
  noop: Re,
  safe_not_equal: pl,
  svg_element: ot
} = window.__gradio__svelte__internal;
function yl(l) {
  let e, t;
  return {
    c() {
      e = ot("svg"), t = ot("polyline"), le(t, "points", "20 6 9 17 4 12"), le(e, "xmlns", "http://www.w3.org/2000/svg"), le(e, "viewBox", "2 0 20 20"), le(e, "fill", "none"), le(e, "stroke", "currentColor"), le(e, "stroke-width", "3"), le(e, "stroke-linecap", "round"), le(e, "stroke-linejoin", "round");
    },
    m(n, i) {
      vl(n, e, i), gl(e, t);
    },
    p: Re,
    i: Re,
    o: Re,
    d(n) {
      n && wl(e);
    }
  };
}
class Cl extends bl {
  constructor(e) {
    super(), kl(this, e, null, yl, pl, {});
  }
}
const {
  SvelteComponent: ql,
  append: ft,
  attr: ae,
  detach: Tl,
  init: Ll,
  insert: Sl,
  noop: Ae,
  safe_not_equal: Fl,
  svg_element: De
} = window.__gradio__svelte__internal;
function Hl(l) {
  let e, t, n;
  return {
    c() {
      e = De("svg"), t = De("path"), n = De("path"), ae(t, "fill", "currentColor"), ae(t, "d", "M28 10v18H10V10h18m0-2H10a2 2 0 0 0-2 2v18a2 2 0 0 0 2 2h18a2 2 0 0 0 2-2V10a2 2 0 0 0-2-2Z"), ae(n, "fill", "currentColor"), ae(n, "d", "M4 18H2V4a2 2 0 0 1 2-2h14v2H4Z"), ae(e, "xmlns", "http://www.w3.org/2000/svg"), ae(e, "viewBox", "0 0 33 33"), ae(e, "color", "currentColor");
    },
    m(i, s) {
      Sl(i, e, s), ft(e, t), ft(e, n);
    },
    p: Ae,
    i: Ae,
    o: Ae,
    d(i) {
      i && Tl(e);
    }
  };
}
class Ml extends ql {
  constructor(e) {
    super(), Ll(this, e, null, Hl, Fl, {});
  }
}
function Ee() {
}
const jl = (l) => l;
function Nl(l, e) {
  return l != l ? e == e : l !== e || l && typeof l == "object" || typeof l == "function";
}
const It = typeof window < "u";
let _t = It ? () => window.performance.now() : () => Date.now(), Wt = It ? (l) => requestAnimationFrame(l) : Ee;
const Ce = /* @__PURE__ */ new Set();
function Ut(l) {
  Ce.forEach((e) => {
    e.c(l) || (Ce.delete(e), e.f());
  }), Ce.size !== 0 && Wt(Ut);
}
function Vl(l) {
  let e;
  return Ce.size === 0 && Wt(Ut), {
    promise: new Promise((t) => {
      Ce.add(e = { c: l, f: t });
    }),
    abort() {
      Ce.delete(e);
    }
  };
}
function zl(l, { delay: e = 0, duration: t = 400, easing: n = jl } = {}) {
  const i = +getComputedStyle(l).opacity;
  return {
    delay: e,
    duration: t,
    easing: n,
    css: (s) => `opacity: ${s * i}`
  };
}
const ve = [];
function Bl(l, e = Ee) {
  let t;
  const n = /* @__PURE__ */ new Set();
  function i(r) {
    if (Nl(l, r) && (l = r, t)) {
      const a = !ve.length;
      for (const f of n)
        f[1](), ve.push(f, l);
      if (a) {
        for (let f = 0; f < ve.length; f += 2)
          ve[f][0](ve[f + 1]);
        ve.length = 0;
      }
    }
  }
  function s(r) {
    i(r(l));
  }
  function o(r, a = Ee) {
    const f = [r, a];
    return n.add(f), n.size === 1 && (t = e(i, s) || Ee), r(l), () => {
      n.delete(f), n.size === 0 && t && (t(), t = null);
    };
  }
  return { set: i, update: s, subscribe: o };
}
function at(l) {
  return Object.prototype.toString.call(l) === "[object Date]";
}
function We(l, e, t, n) {
  if (typeof t == "number" || at(t)) {
    const i = n - t, s = (t - e) / (l.dt || 1 / 60), o = l.opts.stiffness * i, r = l.opts.damping * s, a = (o - r) * l.inv_mass, f = (s + a) * l.dt;
    return Math.abs(f) < l.opts.precision && Math.abs(i) < l.opts.precision ? n : (l.settled = !1, at(t) ? new Date(t.getTime() + f) : t + f);
  } else {
    if (Array.isArray(t))
      return t.map(
        (i, s) => We(l, e[s], t[s], n[s])
      );
    if (typeof t == "object") {
      const i = {};
      for (const s in t)
        i[s] = We(l, e[s], t[s], n[s]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function rt(l, e = {}) {
  const t = Bl(l), { stiffness: n = 0.15, damping: i = 0.8, precision: s = 0.01 } = e;
  let o, r, a, f = l, _ = l, u = 1, c = 0, m = !1;
  function y(T, L = {}) {
    _ = T;
    const C = a = {};
    return l == null || L.hard || S.stiffness >= 1 && S.damping >= 1 ? (m = !0, o = _t(), f = T, t.set(l = _), Promise.resolve()) : (L.soft && (c = 1 / ((L.soft === !0 ? 0.5 : +L.soft) * 60), u = 0), r || (o = _t(), m = !1, r = Vl((d) => {
      if (m)
        return m = !1, r = null, !1;
      u = Math.min(u + c, 1);
      const p = {
        inv_mass: u,
        opts: S,
        settled: !0,
        dt: (d - o) * 60 / 1e3
      }, H = We(p, f, l, _);
      return o = d, f = l, t.set(l = H), p.settled && (r = null), !p.settled;
    })), new Promise((d) => {
      r.promise.then(() => {
        C === a && d();
      });
    }));
  }
  const S = {
    set: y,
    update: (T, L) => y(T(_, l), L),
    subscribe: t.subscribe,
    stiffness: n,
    damping: i,
    precision: s
  };
  return S;
}
const ut = [
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
], ct = {
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
}, dt = El.reduce(
  (l, { color: e, primary: t, secondary: n }) => ({
    ...l,
    [e]: {
      primary: ct[e][t],
      secondary: ct[e][n]
    }
  }),
  {}
), Pl = (l) => ut[l % ut.length];
function mt(l, e, t) {
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
    s in dt ? n[i] = dt[s] : n[i] = {
      primary: e ? mt(l[i], 1, t) : l[i],
      secondary: e ? mt(l[i], 0.5, t) : l[i]
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
function Al(l, e) {
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
  SvelteComponent: Dl,
  add_render_callback: Ge,
  append: ht,
  attr: B,
  binding_callbacks: bt,
  bubble: Se,
  check_outros: Xt,
  create_component: Je,
  create_in_transition: Il,
  destroy_component: Ke,
  detach: de,
  element: Me,
  empty: Wl,
  group_outros: Yt,
  init: Ul,
  insert: me,
  listen: Y,
  mount_component: Qe,
  noop: Gt,
  run_all: Xl,
  safe_not_equal: Yl,
  set_data: Gl,
  space: gt,
  text: Jl,
  toggle_class: wt,
  transition_in: ie,
  transition_out: ce
} = window.__gradio__svelte__internal, { beforeUpdate: Kl, afterUpdate: Ql, createEventDispatcher: xl } = window.__gradio__svelte__internal;
function $l(l) {
  let e;
  return {
    c() {
      e = Jl(
        /*label*/
        l[0]
      );
    },
    m(t, n) {
      me(t, e, n);
    },
    p(t, n) {
      n[0] & /*label*/
      1 && Gl(
        e,
        /*label*/
        t[0]
      );
    },
    d(t) {
      t && de(e);
    }
  };
}
function kt(l) {
  let e, t, n, i;
  const s = [tn, en], o = [];
  function r(a, f) {
    return (
      /*copied*/
      a[13] ? 0 : 1
    );
  }
  return e = r(l), t = o[e] = s[e](l), {
    c() {
      t.c(), n = Wl();
    },
    m(a, f) {
      o[e].m(a, f), me(a, n, f), i = !0;
    },
    p(a, f) {
      let _ = e;
      e = r(a), e === _ ? o[e].p(a, f) : (Yt(), ce(o[_], 1, 1, () => {
        o[_] = null;
      }), Xt(), t = o[e], t ? t.p(a, f) : (t = o[e] = s[e](a), t.c()), ie(t, 1), t.m(n.parentNode, n));
    },
    i(a) {
      i || (ie(t), i = !0);
    },
    o(a) {
      ce(t), i = !1;
    },
    d(a) {
      a && de(n), o[e].d(a);
    }
  };
}
function en(l) {
  let e, t, n, i, s;
  return t = new Ml({}), {
    c() {
      e = Me("button"), Je(t.$$.fragment), B(e, "aria-label", "Copy"), B(e, "aria-roledescription", "Copy text"), B(e, "class", "svelte-40uavx");
    },
    m(o, r) {
      me(o, e, r), Qe(t, e, null), n = !0, i || (s = Y(
        e,
        "click",
        /*handle_copy*/
        l[15]
      ), i = !0);
    },
    p: Gt,
    i(o) {
      n || (ie(t.$$.fragment, o), n = !0);
    },
    o(o) {
      ce(t.$$.fragment, o), n = !1;
    },
    d(o) {
      o && de(e), Ke(t), i = !1, s();
    }
  };
}
function tn(l) {
  let e, t, n, i;
  return t = new Cl({}), {
    c() {
      e = Me("button"), Je(t.$$.fragment), B(e, "aria-label", "Copied"), B(e, "aria-roledescription", "Text copied"), B(e, "class", "svelte-40uavx");
    },
    m(s, o) {
      me(s, e, o), Qe(t, e, null), i = !0;
    },
    p: Gt,
    i(s) {
      i || (ie(t.$$.fragment, s), s && (n || Ge(() => {
        n = Il(e, zl, { duration: 300 }), n.start();
      })), i = !0);
    },
    o(s) {
      ce(t.$$.fragment, s), i = !1;
    },
    d(s) {
      s && de(e), Ke(t);
    }
  };
}
function ln(l) {
  let e, t, n;
  return {
    c() {
      e = Me("div"), B(e, "class", "textfield svelte-40uavx"), B(e, "data-testid", "highlighted-textbox"), B(e, "contenteditable", "true"), /*el_text*/
      (l[10] === void 0 || /*marked_el_text*/
      l[11] === void 0) && Ge(() => (
        /*div_input_handler_1*/
        l[27].call(e)
      ));
    },
    m(i, s) {
      me(i, e, s), l[26](e), /*el_text*/
      l[10] !== void 0 && (e.textContent = /*el_text*/
      l[10]), /*marked_el_text*/
      l[11] !== void 0 && (e.innerHTML = /*marked_el_text*/
      l[11]), t || (n = [
        Y(
          e,
          "input",
          /*div_input_handler_1*/
          l[27]
        ),
        Y(
          e,
          "blur",
          /*blur_handler*/
          l[19]
        ),
        Y(
          e,
          "keypress",
          /*keypress_handler*/
          l[20]
        ),
        Y(
          e,
          "select",
          /*select_handler*/
          l[21]
        ),
        Y(
          e,
          "scroll",
          /*scroll_handler*/
          l[22]
        ),
        Y(
          e,
          "input",
          /*handle_change*/
          l[14]
        ),
        Y(
          e,
          "focus",
          /*focus_handler*/
          l[23]
        ),
        Y(
          e,
          "change",
          /*handle_change*/
          l[14]
        )
      ], t = !0);
    },
    p(i, s) {
      s[0] & /*el_text*/
      1024 && /*el_text*/
      i[10] !== e.textContent && (e.textContent = /*el_text*/
      i[10]), s[0] & /*marked_el_text*/
      2048 && /*marked_el_text*/
      i[11] !== e.innerHTML && (e.innerHTML = /*marked_el_text*/
      i[11]);
    },
    d(i) {
      i && de(e), l[26](null), t = !1, Xl(n);
    }
  };
}
function nn(l) {
  let e, t, n;
  return {
    c() {
      e = Me("div"), B(e, "class", "textfield svelte-40uavx"), B(e, "data-testid", "highlighted-textbox"), B(e, "contenteditable", "false"), /*el_text*/
      (l[10] === void 0 || /*marked_el_text*/
      l[11] === void 0) && Ge(() => (
        /*div_input_handler*/
        l[25].call(e)
      ));
    },
    m(i, s) {
      me(i, e, s), l[24](e), /*el_text*/
      l[10] !== void 0 && (e.textContent = /*el_text*/
      l[10]), /*marked_el_text*/
      l[11] !== void 0 && (e.innerHTML = /*marked_el_text*/
      l[11]), t || (n = Y(
        e,
        "input",
        /*div_input_handler*/
        l[25]
      ), t = !0);
    },
    p(i, s) {
      s[0] & /*el_text*/
      1024 && /*el_text*/
      i[10] !== e.textContent && (e.textContent = /*el_text*/
      i[10]), s[0] & /*marked_el_text*/
      2048 && /*marked_el_text*/
      i[11] !== e.innerHTML && (e.innerHTML = /*marked_el_text*/
      i[11]);
    },
    d(i) {
      i && de(e), l[24](null), t = !1, n();
    }
  };
}
function sn(l) {
  let e, t, n, i, s;
  t = new hl({
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
      $$slots: { default: [$l] },
      $$scope: { ctx: l }
    }
  });
  let o = (
    /*show_copy_button*/
    l[7] && kt(l)
  );
  function r(_, u) {
    return (
      /*disabled*/
      _[8] ? nn : ln
    );
  }
  let a = r(l), f = a(l);
  return {
    c() {
      e = Me("label"), Je(t.$$.fragment), n = gt(), o && o.c(), i = gt(), f.c(), B(e, "class", "svelte-40uavx"), wt(
        e,
        "container",
        /*container*/
        l[6]
      );
    },
    m(_, u) {
      me(_, e, u), Qe(t, e, null), ht(e, n), o && o.m(e, null), ht(e, i), f.m(e, null), s = !0;
    },
    p(_, u) {
      const c = {};
      u[0] & /*show_label*/
      8 && (c.show_label = /*show_label*/
      _[3]), u[0] & /*show_legend*/
      16 && (c.show_legend = /*show_legend*/
      _[4]), u[0] & /*show_legend_label*/
      32 && (c.show_legend_label = /*show_legend_label*/
      _[5]), u[0] & /*legend_label*/
      2 && (c.legend_label = /*legend_label*/
      _[1]), u[0] & /*_color_map*/
      4096 && (c._color_map = /*_color_map*/
      _[12]), u[0] & /*info*/
      4 && (c.info = /*info*/
      _[2]), u[0] & /*label*/
      1 | u[1] & /*$$scope*/
      256 && (c.$$scope = { dirty: u, ctx: _ }), t.$set(c), /*show_copy_button*/
      _[7] ? o ? (o.p(_, u), u[0] & /*show_copy_button*/
      128 && ie(o, 1)) : (o = kt(_), o.c(), ie(o, 1), o.m(e, i)) : o && (Yt(), ce(o, 1, 1, () => {
        o = null;
      }), Xt()), a === (a = r(_)) && f ? f.p(_, u) : (f.d(1), f = a(_), f && (f.c(), f.m(e, null))), (!s || u[0] & /*container*/
      64) && wt(
        e,
        "container",
        /*container*/
        _[6]
      );
    },
    i(_) {
      s || (ie(t.$$.fragment, _), ie(o), s = !0);
    },
    o(_) {
      ce(t.$$.fragment, _), ce(o), s = !1;
    },
    d(_) {
      _ && de(e), Ke(t), o && o.d(), f.d();
    }
  };
}
function on(l, e, t) {
  const n = typeof document < "u";
  let { value: i = [] } = e, { value_is_output: s = !1 } = e, { label: o } = e, { legend_label: r } = e, { info: a = void 0 } = e, { show_label: f = !0 } = e, { show_legend: _ = !1 } = e, { show_legend_label: u = !1 } = e, { container: c = !0 } = e, { color_map: m = {} } = e, { show_copy_button: y = !1 } = e, { disabled: S } = e, T, L = "", C = "", d, p = !m || Object.keys(m).length === 0 ? {} : m, H = {}, b = !1, R;
  function K() {
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
    i.length > 0 && h && (t(10, L = i.map(([N, j]) => N).join("")), t(11, C = i.map(([N, j]) => j !== null ? `<mark class="hl ${j}" style="background-color:${H[j].secondary}">${N}</mark>` : N).join("")));
  }
  const A = xl();
  Kl(() => {
    T && T.offsetHeight + T.scrollTop > T.scrollHeight - 100;
  });
  function X() {
    P(), he(), A("change", i), s || A("input", i);
  }
  Ql(() => {
    K(), E(s), t(17, s = !1);
  });
  function he() {
    let h = [], N = "", j = null, ee = !1, we = "", ke = C.replace(/&nbsp;|&amp;|&lt;|&gt;/g, function(te) {
      return {
        "&nbsp;": " ",
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">"
      }[te];
    });
    for (let te = 0; te < ke.length; te++) {
      let x = ke[te];
      if (x === "<")
        ee = !0, N && h.push([N, j]), N = "", j = null;
      else if (x === ">") {
        if (ee = !1, we.slice(0, 4) === "mark") {
          let Ve = /class="hl ([^"]+)"/.exec(we);
          j = Ve ? Ve[1] : null;
        }
        we = "";
      } else
        ee ? we += x : N += x;
    }
    N && h.push([N, j]), t(16, i = h);
  }
  async function D() {
    "clipboard" in navigator && (await navigator.clipboard.writeText(L), Q());
  }
  function Q() {
    t(13, b = !0), R && clearTimeout(R), R = setTimeout(
      () => {
        t(13, b = !1);
      },
      1e3
    );
  }
  function P() {
    const h = window.getSelection(), N = h.anchorOffset;
    if (h.rangeCount > 0) {
      var j = h.getRangeAt(0).commonAncestorContainer.parentElement;
      if (j && j.tagName.toLowerCase() === "mark") {
        const Ve = j.textContent;
        var ee = j.parentElement, we = document.createTextNode(Ve);
        ee.replaceChild(we, j), t(11, C = ee.innerHTML);
        var ke = document.createRange(), te = window.getSelection();
        const tl = N + Rl(ee);
        var x = Al(ee, tl);
        ke.setStart(x.node, x.offset), ke.setEnd(x.node, x.offset), te.removeAllRanges(), te.addRange(ke);
      }
    }
  }
  function be(h) {
    Se.call(this, l, h);
  }
  function g(h) {
    Se.call(this, l, h);
  }
  function je(h) {
    Se.call(this, l, h);
  }
  function Ne(h) {
    Se.call(this, l, h);
  }
  function ge(h) {
    Se.call(this, l, h);
  }
  function Ze(h) {
    bt[h ? "unshift" : "push"](() => {
      T = h, t(9, T);
    });
  }
  function Oe() {
    L = this.textContent, C = this.innerHTML, t(10, L), t(11, C);
  }
  function w(h) {
    bt[h ? "unshift" : "push"](() => {
      T = h, t(9, T);
    });
  }
  function el() {
    L = this.textContent, C = this.innerHTML, t(10, L), t(11, C);
  }
  return l.$$set = (h) => {
    "value" in h && t(16, i = h.value), "value_is_output" in h && t(17, s = h.value_is_output), "label" in h && t(0, o = h.label), "legend_label" in h && t(1, r = h.legend_label), "info" in h && t(2, a = h.info), "show_label" in h && t(3, f = h.show_label), "show_legend" in h && t(4, _ = h.show_legend), "show_legend_label" in h && t(5, u = h.show_legend_label), "container" in h && t(6, c = h.container), "color_map" in h && t(18, m = h.color_map), "show_copy_button" in h && t(7, y = h.show_copy_button), "disabled" in h && t(8, S = h.disabled);
  }, K(), E(!0), [
    o,
    r,
    a,
    f,
    _,
    u,
    c,
    y,
    S,
    T,
    L,
    C,
    H,
    b,
    X,
    D,
    i,
    s,
    m,
    be,
    g,
    je,
    Ne,
    ge,
    Ze,
    Oe,
    w,
    el
  ];
}
class fn extends Dl {
  constructor(e) {
    super(), Ul(
      this,
      e,
      on,
      sn,
      Yl,
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
  SvelteComponent: _n,
  assign: an,
  create_slot: rn,
  detach: un,
  element: cn,
  get_all_dirty_from_scope: dn,
  get_slot_changes: mn,
  get_spread_update: hn,
  init: bn,
  insert: gn,
  safe_not_equal: wn,
  set_dynamic_element_data: vt,
  set_style: z,
  toggle_class: ne,
  transition_in: Jt,
  transition_out: Kt,
  update_slot_base: kn
} = window.__gradio__svelte__internal;
function vn(l) {
  let e, t, n;
  const i = (
    /*#slots*/
    l[18].default
  ), s = rn(
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
  for (let a = 0; a < o.length; a += 1)
    r = an(r, o[a]);
  return {
    c() {
      e = cn(
        /*tag*/
        l[14]
      ), s && s.c(), vt(
        /*tag*/
        l[14]
      )(e, r), ne(
        e,
        "hidden",
        /*visible*/
        l[10] === !1
      ), ne(
        e,
        "padded",
        /*padding*/
        l[6]
      ), ne(
        e,
        "border_focus",
        /*border_mode*/
        l[5] === "focus"
      ), ne(e, "hide-container", !/*explicit_call*/
      l[8] && !/*container*/
      l[9]), z(
        e,
        "height",
        /*get_dimension*/
        l[15](
          /*height*/
          l[0]
        )
      ), z(e, "width", typeof /*width*/
      l[1] == "number" ? `calc(min(${/*width*/
      l[1]}px, 100%))` : (
        /*get_dimension*/
        l[15](
          /*width*/
          l[1]
        )
      )), z(
        e,
        "border-style",
        /*variant*/
        l[4]
      ), z(
        e,
        "overflow",
        /*allow_overflow*/
        l[11] ? "visible" : "hidden"
      ), z(
        e,
        "flex-grow",
        /*scale*/
        l[12]
      ), z(e, "min-width", `calc(min(${/*min_width*/
      l[13]}px, 100%))`), z(e, "border-width", "var(--block-border-width)");
    },
    m(a, f) {
      gn(a, e, f), s && s.m(e, null), n = !0;
    },
    p(a, f) {
      s && s.p && (!n || f & /*$$scope*/
      131072) && kn(
        s,
        i,
        a,
        /*$$scope*/
        a[17],
        n ? mn(
          i,
          /*$$scope*/
          a[17],
          f,
          null
        ) : dn(
          /*$$scope*/
          a[17]
        ),
        null
      ), vt(
        /*tag*/
        a[14]
      )(e, r = hn(o, [
        (!n || f & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          a[7]
        ) },
        (!n || f & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          a[2]
        ) },
        (!n || f & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        a[3].join(" ") + " svelte-1t38q2d")) && { class: t }
      ])), ne(
        e,
        "hidden",
        /*visible*/
        a[10] === !1
      ), ne(
        e,
        "padded",
        /*padding*/
        a[6]
      ), ne(
        e,
        "border_focus",
        /*border_mode*/
        a[5] === "focus"
      ), ne(e, "hide-container", !/*explicit_call*/
      a[8] && !/*container*/
      a[9]), f & /*height*/
      1 && z(
        e,
        "height",
        /*get_dimension*/
        a[15](
          /*height*/
          a[0]
        )
      ), f & /*width*/
      2 && z(e, "width", typeof /*width*/
      a[1] == "number" ? `calc(min(${/*width*/
      a[1]}px, 100%))` : (
        /*get_dimension*/
        a[15](
          /*width*/
          a[1]
        )
      )), f & /*variant*/
      16 && z(
        e,
        "border-style",
        /*variant*/
        a[4]
      ), f & /*allow_overflow*/
      2048 && z(
        e,
        "overflow",
        /*allow_overflow*/
        a[11] ? "visible" : "hidden"
      ), f & /*scale*/
      4096 && z(
        e,
        "flex-grow",
        /*scale*/
        a[12]
      ), f & /*min_width*/
      8192 && z(e, "min-width", `calc(min(${/*min_width*/
      a[13]}px, 100%))`);
    },
    i(a) {
      n || (Jt(s, a), n = !0);
    },
    o(a) {
      Kt(s, a), n = !1;
    },
    d(a) {
      a && un(e), s && s.d(a);
    }
  };
}
function pn(l) {
  let e, t = (
    /*tag*/
    l[14] && vn(l)
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
      e || (Jt(t, n), e = !0);
    },
    o(n) {
      Kt(t, n), e = !1;
    },
    d(n) {
      t && t.d(n);
    }
  };
}
function yn(l, e, t) {
  let { $$slots: n = {}, $$scope: i } = e, { height: s = void 0 } = e, { width: o = void 0 } = e, { elem_id: r = "" } = e, { elem_classes: a = [] } = e, { variant: f = "solid" } = e, { border_mode: _ = "base" } = e, { padding: u = !0 } = e, { type: c = "normal" } = e, { test_id: m = void 0 } = e, { explicit_call: y = !1 } = e, { container: S = !0 } = e, { visible: T = !0 } = e, { allow_overflow: L = !0 } = e, { scale: C = null } = e, { min_width: d = 0 } = e, p = c === "fieldset" ? "fieldset" : "div";
  const H = (b) => {
    if (b !== void 0) {
      if (typeof b == "number")
        return b + "px";
      if (typeof b == "string")
        return b;
    }
  };
  return l.$$set = (b) => {
    "height" in b && t(0, s = b.height), "width" in b && t(1, o = b.width), "elem_id" in b && t(2, r = b.elem_id), "elem_classes" in b && t(3, a = b.elem_classes), "variant" in b && t(4, f = b.variant), "border_mode" in b && t(5, _ = b.border_mode), "padding" in b && t(6, u = b.padding), "type" in b && t(16, c = b.type), "test_id" in b && t(7, m = b.test_id), "explicit_call" in b && t(8, y = b.explicit_call), "container" in b && t(9, S = b.container), "visible" in b && t(10, T = b.visible), "allow_overflow" in b && t(11, L = b.allow_overflow), "scale" in b && t(12, C = b.scale), "min_width" in b && t(13, d = b.min_width), "$$scope" in b && t(17, i = b.$$scope);
  }, [
    s,
    o,
    r,
    a,
    f,
    _,
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
class Cn extends _n {
  constructor(e) {
    super(), bn(this, e, yn, pn, wn, {
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
function pe(l) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; l > 1e3 && t < e.length - 1; )
    l /= 1e3, t++;
  let n = e[t];
  return (Number.isInteger(l) ? l : l.toFixed(1)) + n;
}
const {
  SvelteComponent: qn,
  append: I,
  attr: q,
  component_subscribe: pt,
  detach: Tn,
  element: Ln,
  init: Sn,
  insert: Fn,
  noop: yt,
  safe_not_equal: Hn,
  set_style: ze,
  svg_element: W,
  toggle_class: Ct
} = window.__gradio__svelte__internal, { onMount: Mn } = window.__gradio__svelte__internal;
function jn(l) {
  let e, t, n, i, s, o, r, a, f, _, u, c;
  return {
    c() {
      e = Ln("div"), t = W("svg"), n = W("g"), i = W("path"), s = W("path"), o = W("path"), r = W("path"), a = W("g"), f = W("path"), _ = W("path"), u = W("path"), c = W("path"), q(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), q(i, "fill", "#FF7C00"), q(i, "fill-opacity", "0.4"), q(i, "class", "svelte-43sxxs"), q(s, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), q(s, "fill", "#FF7C00"), q(s, "class", "svelte-43sxxs"), q(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), q(o, "fill", "#FF7C00"), q(o, "fill-opacity", "0.4"), q(o, "class", "svelte-43sxxs"), q(r, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), q(r, "fill", "#FF7C00"), q(r, "class", "svelte-43sxxs"), ze(n, "transform", "translate(" + /*$top*/
      l[1][0] + "px, " + /*$top*/
      l[1][1] + "px)"), q(f, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), q(f, "fill", "#FF7C00"), q(f, "fill-opacity", "0.4"), q(f, "class", "svelte-43sxxs"), q(_, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), q(_, "fill", "#FF7C00"), q(_, "class", "svelte-43sxxs"), q(u, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), q(u, "fill", "#FF7C00"), q(u, "fill-opacity", "0.4"), q(u, "class", "svelte-43sxxs"), q(c, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), q(c, "fill", "#FF7C00"), q(c, "class", "svelte-43sxxs"), ze(a, "transform", "translate(" + /*$bottom*/
      l[2][0] + "px, " + /*$bottom*/
      l[2][1] + "px)"), q(t, "viewBox", "-1200 -1200 3000 3000"), q(t, "fill", "none"), q(t, "xmlns", "http://www.w3.org/2000/svg"), q(t, "class", "svelte-43sxxs"), q(e, "class", "svelte-43sxxs"), Ct(
        e,
        "margin",
        /*margin*/
        l[0]
      );
    },
    m(m, y) {
      Fn(m, e, y), I(e, t), I(t, n), I(n, i), I(n, s), I(n, o), I(n, r), I(t, a), I(a, f), I(a, _), I(a, u), I(a, c);
    },
    p(m, [y]) {
      y & /*$top*/
      2 && ze(n, "transform", "translate(" + /*$top*/
      m[1][0] + "px, " + /*$top*/
      m[1][1] + "px)"), y & /*$bottom*/
      4 && ze(a, "transform", "translate(" + /*$bottom*/
      m[2][0] + "px, " + /*$bottom*/
      m[2][1] + "px)"), y & /*margin*/
      1 && Ct(
        e,
        "margin",
        /*margin*/
        m[0]
      );
    },
    i: yt,
    o: yt,
    d(m) {
      m && Tn(e);
    }
  };
}
function Nn(l, e, t) {
  let n, i, { margin: s = !0 } = e;
  const o = rt([0, 0]);
  pt(l, o, (c) => t(1, n = c));
  const r = rt([0, 0]);
  pt(l, r, (c) => t(2, i = c));
  let a;
  async function f() {
    await Promise.all([o.set([125, 140]), r.set([-125, -140])]), await Promise.all([o.set([-125, 140]), r.set([125, -140])]), await Promise.all([o.set([-125, 0]), r.set([125, -0])]), await Promise.all([o.set([125, 0]), r.set([-125, 0])]);
  }
  async function _() {
    await f(), a || _();
  }
  async function u() {
    await Promise.all([o.set([125, 0]), r.set([-125, 0])]), _();
  }
  return Mn(() => (u(), () => a = !0)), l.$$set = (c) => {
    "margin" in c && t(0, s = c.margin);
  }, [s, n, i, o, r];
}
class Vn extends qn {
  constructor(e) {
    super(), Sn(this, e, Nn, jn, Hn, { margin: 0 });
  }
}
const {
  SvelteComponent: zn,
  append: re,
  attr: G,
  binding_callbacks: qt,
  check_outros: Qt,
  create_component: Bn,
  create_slot: En,
  destroy_component: Pn,
  destroy_each: xt,
  detach: k,
  element: $,
  empty: Le,
  ensure_array_like: Pe,
  get_all_dirty_from_scope: Zn,
  get_slot_changes: On,
  group_outros: $t,
  init: Rn,
  insert: v,
  mount_component: An,
  noop: Ue,
  safe_not_equal: Dn,
  set_data: O,
  set_style: se,
  space: J,
  text: F,
  toggle_class: Z,
  transition_in: qe,
  transition_out: Te,
  update_slot_base: In
} = window.__gradio__svelte__internal, { tick: Wn } = window.__gradio__svelte__internal, { onDestroy: Un } = window.__gradio__svelte__internal, Xn = (l) => ({}), Tt = (l) => ({});
function Lt(l, e, t) {
  const n = l.slice();
  return n[38] = e[t], n[40] = t, n;
}
function St(l, e, t) {
  const n = l.slice();
  return n[38] = e[t], n;
}
function Yn(l) {
  let e, t = (
    /*i18n*/
    l[1]("common.error") + ""
  ), n, i, s;
  const o = (
    /*#slots*/
    l[29].error
  ), r = En(
    o,
    l,
    /*$$scope*/
    l[28],
    Tt
  );
  return {
    c() {
      e = $("span"), n = F(t), i = J(), r && r.c(), G(e, "class", "error svelte-1txqlrd");
    },
    m(a, f) {
      v(a, e, f), re(e, n), v(a, i, f), r && r.m(a, f), s = !0;
    },
    p(a, f) {
      (!s || f[0] & /*i18n*/
      2) && t !== (t = /*i18n*/
      a[1]("common.error") + "") && O(n, t), r && r.p && (!s || f[0] & /*$$scope*/
      268435456) && In(
        r,
        o,
        a,
        /*$$scope*/
        a[28],
        s ? On(
          o,
          /*$$scope*/
          a[28],
          f,
          Xn
        ) : Zn(
          /*$$scope*/
          a[28]
        ),
        Tt
      );
    },
    i(a) {
      s || (qe(r, a), s = !0);
    },
    o(a) {
      Te(r, a), s = !1;
    },
    d(a) {
      a && (k(e), k(i)), r && r.d(a);
    }
  };
}
function Gn(l) {
  let e, t, n, i, s, o, r, a, f, _ = (
    /*variant*/
    l[8] === "default" && /*show_eta_bar*/
    l[18] && /*show_progress*/
    l[6] === "full" && Ft(l)
  );
  function u(d, p) {
    if (
      /*progress*/
      d[7]
    )
      return Qn;
    if (
      /*queue_position*/
      d[2] !== null && /*queue_size*/
      d[3] !== void 0 && /*queue_position*/
      d[2] >= 0
    )
      return Kn;
    if (
      /*queue_position*/
      d[2] === 0
    )
      return Jn;
  }
  let c = u(l), m = c && c(l), y = (
    /*timer*/
    l[5] && jt(l)
  );
  const S = [ti, ei], T = [];
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
  l[5] && Zt(l);
  return {
    c() {
      _ && _.c(), e = J(), t = $("div"), m && m.c(), n = J(), y && y.c(), i = J(), o && o.c(), r = J(), C && C.c(), a = Le(), G(t, "class", "progress-text svelte-1txqlrd"), Z(
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
      _ && _.m(d, p), v(d, e, p), v(d, t, p), m && m.m(t, null), re(t, n), y && y.m(t, null), v(d, i, p), ~s && T[s].m(d, p), v(d, r, p), C && C.m(d, p), v(d, a, p), f = !0;
    },
    p(d, p) {
      /*variant*/
      d[8] === "default" && /*show_eta_bar*/
      d[18] && /*show_progress*/
      d[6] === "full" ? _ ? _.p(d, p) : (_ = Ft(d), _.c(), _.m(e.parentNode, e)) : _ && (_.d(1), _ = null), c === (c = u(d)) && m ? m.p(d, p) : (m && m.d(1), m = c && c(d), m && (m.c(), m.m(t, n))), /*timer*/
      d[5] ? y ? y.p(d, p) : (y = jt(d), y.c(), y.m(t, null)) : y && (y.d(1), y = null), (!f || p[0] & /*variant*/
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
      s = L(d), s === H ? ~s && T[s].p(d, p) : (o && ($t(), Te(T[H], 1, 1, () => {
        T[H] = null;
      }), Qt()), ~s ? (o = T[s], o ? o.p(d, p) : (o = T[s] = S[s](d), o.c()), qe(o, 1), o.m(r.parentNode, r)) : o = null), /*timer*/
      d[5] ? C && (C.d(1), C = null) : C ? C.p(d, p) : (C = Zt(d), C.c(), C.m(a.parentNode, a));
    },
    i(d) {
      f || (qe(o), f = !0);
    },
    o(d) {
      Te(o), f = !1;
    },
    d(d) {
      d && (k(e), k(t), k(i), k(r), k(a)), _ && _.d(d), m && m.d(), y && y.d(), ~s && T[s].d(d), C && C.d(d);
    }
  };
}
function Ft(l) {
  let e, t = `translateX(${/*eta_level*/
  (l[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = $("div"), G(e, "class", "eta-bar svelte-1txqlrd"), se(e, "transform", t);
    },
    m(n, i) {
      v(n, e, i);
    },
    p(n, i) {
      i[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (n[17] || 0) * 100 - 100}%)`) && se(e, "transform", t);
    },
    d(n) {
      n && k(e);
    }
  };
}
function Jn(l) {
  let e;
  return {
    c() {
      e = F("processing |");
    },
    m(t, n) {
      v(t, e, n);
    },
    p: Ue,
    d(t) {
      t && k(e);
    }
  };
}
function Kn(l) {
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
    m(r, a) {
      v(r, e, a), v(r, n, a), v(r, i, a), v(r, s, a), v(r, o, a);
    },
    p(r, a) {
      a[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      r[2] + 1 + "") && O(n, t), a[0] & /*queue_size*/
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
function Qn(l) {
  let e, t = Pe(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = Mt(St(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = Le();
    },
    m(i, s) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, s);
      v(i, e, s);
    },
    p(i, s) {
      if (s[0] & /*progress*/
      128) {
        t = Pe(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const r = St(i, t, o);
          n[o] ? n[o].p(r, s) : (n[o] = Mt(r), n[o].c(), n[o].m(e.parentNode, e));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && k(e), xt(n, i);
    }
  };
}
function Ht(l) {
  let e, t = (
    /*p*/
    l[38].unit + ""
  ), n, i, s = " ", o;
  function r(_, u) {
    return (
      /*p*/
      _[38].length != null ? $n : xn
    );
  }
  let a = r(l), f = a(l);
  return {
    c() {
      f.c(), e = J(), n = F(t), i = F(" | "), o = F(s);
    },
    m(_, u) {
      f.m(_, u), v(_, e, u), v(_, n, u), v(_, i, u), v(_, o, u);
    },
    p(_, u) {
      a === (a = r(_)) && f ? f.p(_, u) : (f.d(1), f = a(_), f && (f.c(), f.m(e.parentNode, e))), u[0] & /*progress*/
      128 && t !== (t = /*p*/
      _[38].unit + "") && O(n, t);
    },
    d(_) {
      _ && (k(e), k(n), k(i), k(o)), f.d(_);
    }
  };
}
function xn(l) {
  let e = pe(
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
      128 && e !== (e = pe(
        /*p*/
        n[38].index || 0
      ) + "") && O(t, e);
    },
    d(n) {
      n && k(t);
    }
  };
}
function $n(l) {
  let e = pe(
    /*p*/
    l[38].index || 0
  ) + "", t, n, i = pe(
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
      128 && e !== (e = pe(
        /*p*/
        o[38].index || 0
      ) + "") && O(t, e), r[0] & /*progress*/
      128 && i !== (i = pe(
        /*p*/
        o[38].length
      ) + "") && O(s, i);
    },
    d(o) {
      o && (k(t), k(n), k(s));
    }
  };
}
function Mt(l) {
  let e, t = (
    /*p*/
    l[38].index != null && Ht(l)
  );
  return {
    c() {
      t && t.c(), e = Le();
    },
    m(n, i) {
      t && t.m(n, i), v(n, e, i);
    },
    p(n, i) {
      /*p*/
      n[38].index != null ? t ? t.p(n, i) : (t = Ht(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && k(e), t && t.d(n);
    }
  };
}
function jt(l) {
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
function ei(l) {
  let e, t;
  return e = new Vn({
    props: { margin: (
      /*variant*/
      l[8] === "default"
    ) }
  }), {
    c() {
      Bn(e.$$.fragment);
    },
    m(n, i) {
      An(e, n, i), t = !0;
    },
    p(n, i) {
      const s = {};
      i[0] & /*variant*/
      256 && (s.margin = /*variant*/
      n[8] === "default"), e.$set(s);
    },
    i(n) {
      t || (qe(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Te(e.$$.fragment, n), t = !1;
    },
    d(n) {
      Pn(e, n);
    }
  };
}
function ti(l) {
  let e, t, n, i, s, o = `${/*last_progress_level*/
  l[15] * 100}%`, r = (
    /*progress*/
    l[7] != null && Nt(l)
  );
  return {
    c() {
      e = $("div"), t = $("div"), r && r.c(), n = J(), i = $("div"), s = $("div"), G(t, "class", "progress-level-inner svelte-1txqlrd"), G(s, "class", "progress-bar svelte-1txqlrd"), se(s, "width", o), G(i, "class", "progress-bar-wrap svelte-1txqlrd"), G(e, "class", "progress-level svelte-1txqlrd");
    },
    m(a, f) {
      v(a, e, f), re(e, t), r && r.m(t, null), re(e, n), re(e, i), re(i, s), l[30](s);
    },
    p(a, f) {
      /*progress*/
      a[7] != null ? r ? r.p(a, f) : (r = Nt(a), r.c(), r.m(t, null)) : r && (r.d(1), r = null), f[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      a[15] * 100}%`) && se(s, "width", o);
    },
    i: Ue,
    o: Ue,
    d(a) {
      a && k(e), r && r.d(), l[30](null);
    }
  };
}
function Nt(l) {
  let e, t = Pe(
    /*progress*/
    l[7]
  ), n = [];
  for (let i = 0; i < t.length; i += 1)
    n[i] = Pt(Lt(l, t, i));
  return {
    c() {
      for (let i = 0; i < n.length; i += 1)
        n[i].c();
      e = Le();
    },
    m(i, s) {
      for (let o = 0; o < n.length; o += 1)
        n[o] && n[o].m(i, s);
      v(i, e, s);
    },
    p(i, s) {
      if (s[0] & /*progress_level, progress*/
      16512) {
        t = Pe(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const r = Lt(i, t, o);
          n[o] ? n[o].p(r, s) : (n[o] = Pt(r), n[o].c(), n[o].m(e.parentNode, e));
        }
        for (; o < n.length; o += 1)
          n[o].d(1);
        n.length = t.length;
      }
    },
    d(i) {
      i && k(e), xt(n, i);
    }
  };
}
function Vt(l) {
  let e, t, n, i, s = (
    /*i*/
    l[40] !== 0 && li()
  ), o = (
    /*p*/
    l[38].desc != null && zt(l)
  ), r = (
    /*p*/
    l[38].desc != null && /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[40]
    ] != null && Bt()
  ), a = (
    /*progress_level*/
    l[14] != null && Et(l)
  );
  return {
    c() {
      s && s.c(), e = J(), o && o.c(), t = J(), r && r.c(), n = J(), a && a.c(), i = Le();
    },
    m(f, _) {
      s && s.m(f, _), v(f, e, _), o && o.m(f, _), v(f, t, _), r && r.m(f, _), v(f, n, _), a && a.m(f, _), v(f, i, _);
    },
    p(f, _) {
      /*p*/
      f[38].desc != null ? o ? o.p(f, _) : (o = zt(f), o.c(), o.m(t.parentNode, t)) : o && (o.d(1), o = null), /*p*/
      f[38].desc != null && /*progress_level*/
      f[14] && /*progress_level*/
      f[14][
        /*i*/
        f[40]
      ] != null ? r || (r = Bt(), r.c(), r.m(n.parentNode, n)) : r && (r.d(1), r = null), /*progress_level*/
      f[14] != null ? a ? a.p(f, _) : (a = Et(f), a.c(), a.m(i.parentNode, i)) : a && (a.d(1), a = null);
    },
    d(f) {
      f && (k(e), k(t), k(n), k(i)), s && s.d(f), o && o.d(f), r && r.d(f), a && a.d(f);
    }
  };
}
function li(l) {
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
function zt(l) {
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
function Bt(l) {
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
function Et(l) {
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
function Pt(l) {
  let e, t = (
    /*p*/
    (l[38].desc != null || /*progress_level*/
    l[14] && /*progress_level*/
    l[14][
      /*i*/
      l[40]
    ] != null) && Vt(l)
  );
  return {
    c() {
      t && t.c(), e = Le();
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
      ] != null ? t ? t.p(n, i) : (t = Vt(n), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(n) {
      n && k(e), t && t.d(n);
    }
  };
}
function Zt(l) {
  let e, t;
  return {
    c() {
      e = $("p"), t = F(
        /*loading_text*/
        l[9]
      ), G(e, "class", "loading svelte-1txqlrd");
    },
    m(n, i) {
      v(n, e, i), re(e, t);
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
function ni(l) {
  let e, t, n, i, s;
  const o = [Gn, Yn], r = [];
  function a(f, _) {
    return (
      /*status*/
      f[4] === "pending" ? 0 : (
        /*status*/
        f[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = a(l)) && (n = r[t] = o[t](l)), {
    c() {
      e = $("div"), n && n.c(), G(e, "class", i = "wrap " + /*variant*/
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
      ), se(
        e,
        "position",
        /*absolute*/
        l[10] ? "absolute" : "static"
      ), se(
        e,
        "padding",
        /*absolute*/
        l[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(f, _) {
      v(f, e, _), ~t && r[t].m(e, null), l[31](e), s = !0;
    },
    p(f, _) {
      let u = t;
      t = a(f), t === u ? ~t && r[t].p(f, _) : (n && ($t(), Te(r[u], 1, 1, () => {
        r[u] = null;
      }), Qt()), ~t ? (n = r[t], n ? n.p(f, _) : (n = r[t] = o[t](f), n.c()), qe(n, 1), n.m(e, null)) : n = null), (!s || _[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      f[8] + " " + /*show_progress*/
      f[6] + " svelte-1txqlrd")) && G(e, "class", i), (!s || _[0] & /*variant, show_progress, status, show_progress*/
      336) && Z(e, "hide", !/*status*/
      f[4] || /*status*/
      f[4] === "complete" || /*show_progress*/
      f[6] === "hidden"), (!s || _[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && Z(
        e,
        "translucent",
        /*variant*/
        f[8] === "center" && /*status*/
        (f[4] === "pending" || /*status*/
        f[4] === "error") || /*translucent*/
        f[11] || /*show_progress*/
        f[6] === "minimal"
      ), (!s || _[0] & /*variant, show_progress, status*/
      336) && Z(
        e,
        "generating",
        /*status*/
        f[4] === "generating"
      ), (!s || _[0] & /*variant, show_progress, border*/
      4416) && Z(
        e,
        "border",
        /*border*/
        f[12]
      ), _[0] & /*absolute*/
      1024 && se(
        e,
        "position",
        /*absolute*/
        f[10] ? "absolute" : "static"
      ), _[0] & /*absolute*/
      1024 && se(
        e,
        "padding",
        /*absolute*/
        f[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(f) {
      s || (qe(n), s = !0);
    },
    o(f) {
      Te(n), s = !1;
    },
    d(f) {
      f && k(e), ~t && r[t].d(), l[31](null);
    }
  };
}
let Be = [], Ie = !1;
async function ii(l, e = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && e !== !0)) {
    if (Be.push(l), !Ie)
      Ie = !0;
    else
      return;
    await Wn(), requestAnimationFrame(() => {
      let t = [0, 0];
      for (let n = 0; n < Be.length; n++) {
        const s = Be[n].getBoundingClientRect();
        (n === 0 || s.top + window.scrollY <= t[0]) && (t[0] = s.top + window.scrollY, t[1] = n);
      }
      window.scrollTo({ top: t[0] - 20, behavior: "smooth" }), Ie = !1, Be = [];
    });
  }
}
function si(l, e, t) {
  let n, { $$slots: i = {}, $$scope: s } = e, { i18n: o } = e, { eta: r = null } = e, { queue_position: a } = e, { queue_size: f } = e, { status: _ } = e, { scroll_to_output: u = !1 } = e, { timer: c = !0 } = e, { show_progress: m = "full" } = e, { message: y = null } = e, { progress: S = null } = e, { variant: T = "default" } = e, { loading_text: L = "Loading..." } = e, { absolute: C = !0 } = e, { translucent: d = !1 } = e, { border: p = !1 } = e, { autoscroll: H } = e, b, R = !1, K = 0, E = 0, A = null, X = null, he = 0, D = null, Q, P = null, be = !0;
  const g = () => {
    t(0, r = t(26, A = t(19, ge = null))), t(24, K = performance.now()), t(25, E = 0), R = !0, je();
  };
  function je() {
    requestAnimationFrame(() => {
      t(25, E = (performance.now() - K) / 1e3), R && je();
    });
  }
  function Ne() {
    t(25, E = 0), t(0, r = t(26, A = t(19, ge = null))), R && (R = !1);
  }
  Un(() => {
    R && Ne();
  });
  let ge = null;
  function Ze(w) {
    qt[w ? "unshift" : "push"](() => {
      P = w, t(16, P), t(7, S), t(14, D), t(15, Q);
    });
  }
  function Oe(w) {
    qt[w ? "unshift" : "push"](() => {
      b = w, t(13, b);
    });
  }
  return l.$$set = (w) => {
    "i18n" in w && t(1, o = w.i18n), "eta" in w && t(0, r = w.eta), "queue_position" in w && t(2, a = w.queue_position), "queue_size" in w && t(3, f = w.queue_size), "status" in w && t(4, _ = w.status), "scroll_to_output" in w && t(21, u = w.scroll_to_output), "timer" in w && t(5, c = w.timer), "show_progress" in w && t(6, m = w.show_progress), "message" in w && t(22, y = w.message), "progress" in w && t(7, S = w.progress), "variant" in w && t(8, T = w.variant), "loading_text" in w && t(9, L = w.loading_text), "absolute" in w && t(10, C = w.absolute), "translucent" in w && t(11, d = w.translucent), "border" in w && t(12, p = w.border), "autoscroll" in w && t(23, H = w.autoscroll), "$$scope" in w && t(28, s = w.$$scope);
  }, l.$$.update = () => {
    l.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    218103809 && (r === null && t(0, r = A), r != null && A !== r && (t(27, X = (performance.now() - K) / 1e3 + r), t(19, ge = X.toFixed(1)), t(26, A = r))), l.$$.dirty[0] & /*eta_from_start, timer_diff*/
    167772160 && t(17, he = X === null || X <= 0 || !E ? null : Math.min(E / X, 1)), l.$$.dirty[0] & /*progress*/
    128 && S != null && t(18, be = !1), l.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (S != null ? t(14, D = S.map((w) => {
      if (w.index != null && w.length != null)
        return w.index / w.length;
      if (w.progress != null)
        return w.progress;
    })) : t(14, D = null), D ? (t(15, Q = D[D.length - 1]), P && (Q === 0 ? t(16, P.style.transition = "0", P) : t(16, P.style.transition = "150ms", P))) : t(15, Q = void 0)), l.$$.dirty[0] & /*status*/
    16 && (_ === "pending" ? g() : Ne()), l.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    10493968 && b && u && (_ === "pending" || _ === "complete") && ii(b, H), l.$$.dirty[0] & /*status, message*/
    4194320, l.$$.dirty[0] & /*timer_diff*/
    33554432 && t(20, n = E.toFixed(1));
  }, [
    r,
    o,
    a,
    f,
    _,
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
    Q,
    P,
    he,
    be,
    ge,
    n,
    u,
    y,
    H,
    K,
    E,
    A,
    X,
    s,
    i,
    Ze,
    Oe
  ];
}
class oi extends zn {
  constructor(e) {
    super(), Rn(
      this,
      e,
      si,
      ni,
      Dn,
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
  SvelteComponent: fi,
  add_flush_callback: Ot,
  assign: _i,
  bind: Rt,
  binding_callbacks: At,
  check_outros: ai,
  create_component: xe,
  destroy_component: $e,
  detach: ri,
  flush: M,
  get_spread_object: ui,
  get_spread_update: ci,
  group_outros: di,
  init: mi,
  insert: hi,
  mount_component: et,
  safe_not_equal: bi,
  space: gi,
  transition_in: ye,
  transition_out: Fe
} = window.__gradio__svelte__internal;
function Dt(l) {
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
    i = _i(i, n[s]);
  return e = new oi({ props: i }), {
    c() {
      xe(e.$$.fragment);
    },
    m(s, o) {
      et(e, s, o), t = !0;
    },
    p(s, o) {
      const r = o & /*gradio, loading_status*/
      131080 ? ci(n, [
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
        131072 && ui(
          /*loading_status*/
          s[17]
        )
      ]) : {};
      e.$set(r);
    },
    i(s) {
      t || (ye(e.$$.fragment, s), t = !0);
    },
    o(s) {
      Fe(e.$$.fragment, s), t = !1;
    },
    d(s) {
      $e(e, s);
    }
  };
}
function wi(l) {
  let e, t, n, i, s, o = (
    /*loading_status*/
    l[17] && Dt(l)
  );
  function r(_) {
    l[22](_);
  }
  function a(_) {
    l[23](_);
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
    l[2]), t = new fn({ props: f }), At.push(() => Rt(t, "value", r)), At.push(() => Rt(t, "value_is_output", a)), t.$on(
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
        o && o.c(), e = gi(), xe(t.$$.fragment);
      },
      m(_, u) {
        o && o.m(_, u), hi(_, e, u), et(t, _, u), s = !0;
      },
      p(_, u) {
        /*loading_status*/
        _[17] ? o ? (o.p(_, u), u & /*loading_status*/
        131072 && ye(o, 1)) : (o = Dt(_), o.c(), ye(o, 1), o.m(e.parentNode, e)) : o && (di(), Fe(o, 1, 1, () => {
          o = null;
        }), ai());
        const c = {};
        u & /*label*/
        16 && (c.label = /*label*/
        _[4]), u & /*info*/
        64 && (c.info = /*info*/
        _[6]), u & /*show_label*/
        1024 && (c.show_label = /*show_label*/
        _[10]), u & /*show_legend*/
        2048 && (c.show_legend = /*show_legend*/
        _[11]), u & /*show_legend_label*/
        4096 && (c.show_legend_label = /*show_legend_label*/
        _[12]), u & /*legend_label*/
        32 && (c.legend_label = /*legend_label*/
        _[5]), u & /*color_map*/
        2 && (c.color_map = /*color_map*/
        _[1]), u & /*show_copy_button*/
        65536 && (c.show_copy_button = /*show_copy_button*/
        _[16]), u & /*container*/
        8192 && (c.container = /*container*/
        _[13]), u & /*interactive*/
        262144 && (c.disabled = !/*interactive*/
        _[18]), !n && u & /*value*/
        1 && (n = !0, c.value = /*value*/
        _[0], Ot(() => n = !1)), !i && u & /*value_is_output*/
        4 && (i = !0, c.value_is_output = /*value_is_output*/
        _[2], Ot(() => i = !1)), t.$set(c);
      },
      i(_) {
        s || (ye(o), ye(t.$$.fragment, _), s = !0);
      },
      o(_) {
        Fe(o), Fe(t.$$.fragment, _), s = !1;
      },
      d(_) {
        _ && ri(e), o && o.d(_), $e(t, _);
      }
    }
  );
}
function ki(l) {
  let e, t;
  return e = new Cn({
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
      $$slots: { default: [wi] },
      $$scope: { ctx: l }
    }
  }), {
    c() {
      xe(e.$$.fragment);
    },
    m(n, i) {
      et(e, n, i), t = !0;
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
      t || (ye(e.$$.fragment, n), t = !0);
    },
    o(n) {
      Fe(e.$$.fragment, n), t = !1;
    },
    d(n) {
      $e(e, n);
    }
  };
}
function vi(l, e, t) {
  let { gradio: n } = e, { label: i = "Highlighted Textbox" } = e, { legend_label: s = "Highlights:" } = e, { info: o = void 0 } = e, { elem_id: r = "" } = e, { elem_classes: a = [] } = e, { visible: f = !0 } = e, { value: _ } = e, { show_label: u } = e, { show_legend: c } = e, { show_legend_label: m } = e, { color_map: y = {} } = e, { container: S = !0 } = e, { scale: T = null } = e, { min_width: L = void 0 } = e, { show_copy_button: C = !1 } = e, { loading_status: d = void 0 } = e, { value_is_output: p = !1 } = e, { combine_adjacent: H = !1 } = e, { interactive: b = !0 } = e;
  const R = !1, K = !0;
  function E(g) {
    _ = g, t(0, _), t(19, H);
  }
  function A(g) {
    p = g, t(2, p);
  }
  const X = () => n.dispatch("change"), he = () => n.dispatch("input"), D = () => n.dispatch("submit"), Q = () => n.dispatch("blur"), P = (g) => n.dispatch("select", g.detail), be = () => n.dispatch("focus");
  return l.$$set = (g) => {
    "gradio" in g && t(3, n = g.gradio), "label" in g && t(4, i = g.label), "legend_label" in g && t(5, s = g.legend_label), "info" in g && t(6, o = g.info), "elem_id" in g && t(7, r = g.elem_id), "elem_classes" in g && t(8, a = g.elem_classes), "visible" in g && t(9, f = g.visible), "value" in g && t(0, _ = g.value), "show_label" in g && t(10, u = g.show_label), "show_legend" in g && t(11, c = g.show_legend), "show_legend_label" in g && t(12, m = g.show_legend_label), "color_map" in g && t(1, y = g.color_map), "container" in g && t(13, S = g.container), "scale" in g && t(14, T = g.scale), "min_width" in g && t(15, L = g.min_width), "show_copy_button" in g && t(16, C = g.show_copy_button), "loading_status" in g && t(17, d = g.loading_status), "value_is_output" in g && t(2, p = g.value_is_output), "combine_adjacent" in g && t(19, H = g.combine_adjacent), "interactive" in g && t(18, b = g.interactive);
  }, l.$$.update = () => {
    l.$$.dirty & /*color_map*/
    2 && !y && Object.keys(y).length && t(1, y), l.$$.dirty & /*value, combine_adjacent*/
    524289 && _ && H && t(0, _ = Ol(_, "equal"));
  }, [
    _,
    y,
    p,
    n,
    i,
    s,
    o,
    r,
    a,
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
    K,
    E,
    A,
    X,
    he,
    D,
    Q,
    P,
    be
  ];
}
class pi extends fi {
  constructor(e) {
    super(), mi(this, e, vi, ki, bi, {
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
  pi as default
};
