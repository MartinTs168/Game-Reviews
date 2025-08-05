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

    form.addEventListener('formdata', (event) => {
        // Append Quill content before submitting
        event.formData.append('content', quill.getSemanticHTML());
    });
});