document.addEventListener('DOMContentLoaded', () => {
    const quill = new Quill('#editor', {
        theme: 'snow',
        modules: {
            toolbar: [
                [{'header': [3, false]}],
                ['bold', 'italic', 'underline'],
                [{'list': 'ordered'}, {'list': 'bullet'}],
            ]
        }
    });

    const form = document.querySelector('#review-form');
    quill.clipboard.dangerouslyPasteHTML(document.querySelector('#django-form-container>p>textarea').value)


    form.addEventListener('formdata', (event) => {
        // Append Quill content before submitting
        event.formData.append('content', quill.getSemanticHTML());
    });

    window.addEventListener('resize', function () {
        let toolbar = quill.getModule('toolbar');
        if (toolbar && toolbar.container) {
            toolbar.container.style.maxWidth = '100%';
        }
    });
});