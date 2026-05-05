app.js

document.addEventListener("DOMContentLoaded", () => {

    const body = document.body;
    const menuButton = document.querySelector(".menu-toggle");
    const menu = document.querySelector(".side-menu");
    const backdrop = document.querySelector(".menu-backdrop");
    const shareButton = document.querySelector(".share-button");

    function setMenuState(open) {
        body.classList.toggle("menu-open", open);

        if (menu) {
            menu.setAttribute("aria-hidden", String(!open));
        }

        if (menuButton) {
            menuButton.setAttribute("aria-expanded", String(open));
        }

        if (backdrop) {
            backdrop.hidden = !open;
        }
    }

    // MENU (só roda se existir)
    if (menuButton && menu) {

        menuButton.addEventListener("click", () => {
            const isOpen = body.classList.contains("menu-open");
            setMenuState(!isOpen);
        });

        if (backdrop) {
            backdrop.addEventListener("click", () => setMenuState(false));
        }

        document.addEventListener("keydown", (event) => {
            if (event.key === "Escape") {
                setMenuState(false);
            }
        });

        document.addEventListener("click", (event) => {
            if (!body.classList.contains("menu-open")) return;

            const clickedInsideMenu = menu.contains(event.target);
            const clickedMenuButton = menuButton.contains(event.target);

            if (!clickedInsideMenu && !clickedMenuButton) {
                setMenuState(false);
            }
        });

    } else {
        console.warn("Menu não inicializado (elementos ausentes)");
    }

    // SHARE (independente)
    if (shareButton) {
        shareButton.addEventListener("click", async () => {
            const title = shareButton.dataset.shareTitle || document.title;
            const text = shareButton.dataset.shareText || "";
            const url = shareButton.dataset.shareUrl || window.location.href;

            if (navigator.share) {
                try {
                    await navigator.share({ title, text, url });
                } catch (error) {
                    if (error.name !== "AbortError") {
                        console.error(error);
                    }
                }
            } else {
                try {
                    await navigator.clipboard.writeText(url);
                    alert("Link copiado!");
                } catch (err) {
                    console.error(err);
                }
            }
        });
    }

});