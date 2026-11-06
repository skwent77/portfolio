'use strict';
const projects = window.portfolioProjects;
const dialog = document.querySelector('#project-dialog');
const content = document.querySelector('#dialog-content');
const position = document.querySelector('#project-position');
let currentIndex = 0;
let returnFocus = null;
let sectionHash = '';
let openedFromHash = false;
const escapeHTML = (value) => value.replace(/[&<>"']/g, character => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[character]));

function renderProject(index) {
  currentIndex = (index + projects.length) % projects.length;
  const project = projects[currentIndex];
  content.innerHTML = `<img class="dialog-art" src="./assets/${escapeHTML(project.image)}.svg" alt="${escapeHTML(project.title)} 프로젝트 개념도" width="960" height="540"><article class="dialog-body"><div class="dialog-eyebrow"><span>${escapeHTML(project.category)}</span><span>${escapeHTML(project.year)}</span></div><h2 id="dialog-title">${escapeHTML(project.title)}</h2><p class="dialog-description">${escapeHTML(project.description)}</p><p class="dialog-tags">${escapeHTML(project.tags)}</p><h3>작업 내용</h3><ul>${project.points.map(point => `<li>${escapeHTML(point)}</li>`).join('')}</ul>${project.url ? `<a class="project-source" href="${escapeHTML(project.url)}" target="_blank" rel="noopener noreferrer">View on GitHub ↗</a>` : ''}<p class="source-note">${escapeHTML(project.note)}</p></article>`;
  position.textContent = `${String(currentIndex + 1).padStart(2,'0')} / ${String(projects.length).padStart(2,'0')}`;
  dialog.scrollTop = 0;
}

function openProject(id, fromHash = false) {
  const index = projects.findIndex(project => project.id === id);
  if (index < 0) return;
  if (!dialog.open) {
    returnFocus = document.activeElement;
    sectionHash = location.hash.startsWith('#project/') ? '' : location.hash;
    openedFromHash = fromHash;
    renderProject(index);
    dialog.showModal();
    document.body.classList.add('modal-open');
  } else renderProject(index);
  if (!fromHash) history.pushState({project:id},'',`#project/${id}`);
}

document.querySelectorAll('[data-project]').forEach(button => button.addEventListener('click', () => openProject(button.dataset.project)));
document.querySelector('#close-dialog').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => {
  if (event.target !== dialog) return;
  const bounds = dialog.getBoundingClientRect();
  if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
});
dialog.addEventListener('close', () => {
  document.body.classList.remove('modal-open');
  if (location.hash.startsWith('#project/')) {
    if (openedFromHash) history.replaceState(null,'',location.pathname + location.search + sectionHash);
    else history.back();
  }
  if (returnFocus instanceof HTMLElement) returnFocus.focus({preventScroll:true});
});
function stepProject(direction) {
  renderProject(currentIndex + direction);
  history.replaceState({project:projects[currentIndex].id},'',`#project/${projects[currentIndex].id}`);
}
document.querySelector('#previous-project').addEventListener('click', () => stepProject(-1));
document.querySelector('#next-project').addEventListener('click', () => stepProject(1));
function syncHash() {
  if (location.hash.startsWith('#project/')) openProject(location.hash.slice(9),true);
  else if (dialog.open) dialog.close();
}
window.addEventListener('hashchange', syncHash);
syncHash();
document.querySelector('#year').textContent = new Date().getFullYear();
if ('IntersectionObserver' in window) {
  const links = [...document.querySelectorAll('nav a')];
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      links.forEach(link => {
        if (link.hash === `#${entry.target.id}`) link.setAttribute('aria-current','location');
        else link.removeAttribute('aria-current');
      });
    });
  },{rootMargin:'-10% 0px -65% 0px'});
  document.querySelectorAll('main section[id]').forEach(section => observer.observe(section));
}
