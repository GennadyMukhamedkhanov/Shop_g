from service_objects.services import Service

from products.models.feedbacks import Feedback


class FeedbackListService(Service):

    def process(self):
        return self.get_all_feedback()

    def get_all_feedback(self):
        all_feedback = Feedback.objects.all()
        return all_feedback
