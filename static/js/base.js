(() => {
  const $ = (s, root = document) => root.querySelector(s);

  // Dropdown
  document.querySelectorAll("[data-dropdown]").forEach((dd) => {
    const trigger = dd.querySelector(".dropdown__trigger");
    const menu = dd.querySelector(".dropdown__menu");

    const close = () => {
      dd.classList.remove("is-open");
      trigger?.setAttribute("aria-expanded", "false");
    };

    trigger?.addEventListener("click", (e) => {
      e.stopPropagation();
      const open = !dd.classList.contains("is-open");
      document.querySelectorAll("[data-dropdown].is-open").forEach((x) => x.classList.remove("is-open"));
      if (open) {
        dd.classList.add("is-open");
        trigger.setAttribute("aria-expanded", "true");
      } else {
        close();
      }
    });

    document.addEventListener("click", close);
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") close();
    });

    // prevent click inside menu from closing immediately
    menu?.addEventListener("click", (e) => e.stopPropagation());
  });

  // Mobile drawer
  const drawer = $("#mobileDrawer");
  const openBtn = $("#mobileMenuBtn");
  const closeBtn = $("#mobileCloseBtn");
  const backdrop = $("#drawerBackdrop");

  const openDrawer = () => {
    drawer?.classList.add("is-open");
    drawer?.setAttribute("aria-hidden", "false");
    openBtn?.setAttribute("aria-expanded", "true");
    document.body.style.overflow = "hidden";
  };

  const closeDrawer = () => {
    drawer?.classList.remove("is-open");
    drawer?.setAttribute("aria-hidden", "true");
    openBtn?.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
  };

  openBtn?.addEventListener("click", openDrawer);
  closeBtn?.addEventListener("click", closeDrawer);
  backdrop?.addEventListener("click", closeDrawer);
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeDrawer();
  });

  // Theme toggle (persist)
  const applyTheme = (t) => document.documentElement.setAttribute("data-theme", t);
  const saved = localStorage.getItem("theme");
  if (saved) applyTheme(saved);

  const toggleTheme = () => {
    const current = document.documentElement.getAttribute("data-theme") || "dark";
    const next = current === "dark" ? "light" : "dark";
    applyTheme(next);
    localStorage.setItem("theme", next);
  };

  $("#themeToggle")?.addEventListener("click", toggleTheme);
  $("#drawerThemeToggle")?.addEventListener("click", toggleTheme);
})();