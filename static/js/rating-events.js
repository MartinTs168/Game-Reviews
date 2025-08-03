document.addEventListener('DOMContentLoaded', () => {
    const ratingButtons = document.querySelectorAll(
        '.rating-button');

    const hasRating = window.djangoInfo.currUserRating !== null;

    if (hasRating) {
        document.querySelector(
            `.rating-button[data-value="${window.djangoInfo.currUserRating}"]`
        ).classList.add('selected');

    }

    ratingButtons.forEach(button => {
        button.addEventListener('click', async (event) => {
            const ratingValue = parseInt(event.target.getAttribute(
                'data-value'));

            if (ratingValue < 1 || ratingValue > 5) {
                throw new Error('Invalid rating value');
            }

            try {
                await createRating(ratingValue);
                event.target.classList.add('selected');

            } catch (error) {
                console.log(error);
            }


        })
    })
});

async function createRating(ratingValue) {
    const ratingData = {
        value: ratingValue,
    }

    try {
        const response = await fetch(
            window.djangoInfo.ratingCreateUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': window.djangoInfo.csrfToken,
                },
                body: JSON.stringify(ratingData),
            });
    } catch (error) {
        throw error;
    }
}