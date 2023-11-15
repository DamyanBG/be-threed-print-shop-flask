from models.quote_model import QuoteModel

from cloud.nextcloud import upload_base64_image
from db import db


class QuoteManager:
    @staticmethod
    def select_quote_by_pk(quote_pk):
        quote = QuoteModel.query.filter_by(pk=quote_pk).first()
        return quote

    @staticmethod
    def create_quote(quote_data):
        cad_file = quote_data.pop("cad_file")
        cad_file_url = upload_base64_image(cad_file)
        quote_data["file_path"] = cad_file_url
        quote = QuoteModel(**quote_data)
        db.session.add(quote)
        db.session.commit()
        return quote
