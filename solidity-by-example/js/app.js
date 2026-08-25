(function () {
  const root = document.body;

  function applyTheme(theme) {
    root.classList.remove("light", "dark");
    root.classList.add(theme);
    try {
      localStorage.setItem("sbe-zh-theme", theme);
    } catch (e) {}
    const darkIcon = document.querySelector("[data-icon=dark]");
    const lightIcon = document.querySelector("[data-icon=light]");
    if (darkIcon && lightIcon) {
      darkIcon.hidden = theme !== "dark";
      lightIcon.hidden = theme !== "light";
    }
  }

  function applyNav(open) {
    root.classList.toggle("nav-closed", !open);
    try {
      localStorage.setItem("sbe-zh-nav", open ? "true" : "false");
    } catch (e) {}
  }

  let theme = "light";
  let navOpen = window.innerWidth >= 500;
  try {
    theme = localStorage.getItem("sbe-zh-theme") || "light";
    const storedNav = localStorage.getItem("sbe-zh-nav");
    if (storedNav === "true" || storedNav === "false") {
      navOpen = storedNav === "true";
    }
  } catch (e) {}
  applyTheme(theme);
  applyNav(navOpen);

  const hamburger = document.querySelector("[data-toggle-nav]");
  if (hamburger) {
    hamburger.addEventListener("click", function () {
      navOpen = root.classList.contains("nav-closed");
      applyNav(navOpen);
    });
  }

  const themeBtn = document.querySelector("[data-toggle-theme]");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      theme = root.classList.contains("dark") ? "light" : "dark";
      applyTheme(theme);
    });
  }

  if (window.hljs) {
    document.querySelectorAll("pre code").forEach(function (block) {
      hljs.highlightElement(block);
    });
  }

  document.querySelectorAll("pre").forEach(function (pre) {
    if (pre.querySelector(".copy-btn")) return;
    const btn = document.createElement("button");
    btn.className = "copy-btn";
    btn.type = "button";
    btn.textContent = "copy";
    btn.addEventListener("click", function () {
      const code = pre.querySelector("code");
      const text = code ? code.innerText : pre.innerText;
      navigator.clipboard.writeText(text).then(function () {
        btn.textContent = "copied";
        setTimeout(function () {
          btn.textContent = "copy";
        }, 1200);
      });
    });
    pre.appendChild(btn);
  });

  const search = document.querySelector("[data-search]");
  if (search) {
    const items = document.querySelectorAll("[data-route]");
    search.addEventListener("input", function () {
      const q = search.value.trim().toLowerCase();
      const words = q.split(/\s+/).filter(Boolean);
      items.forEach(function (el) {
        if (!words.length) {
          el.style.display = "";
          return;
        }
        const hay = (el.getAttribute("data-route") || "").toLowerCase();
        const ok = words.every(function (w) {
          return hay.indexOf(w) !== -1;
        });
        el.style.display = ok ? "" : "none";
      });
    });
  }
})();
