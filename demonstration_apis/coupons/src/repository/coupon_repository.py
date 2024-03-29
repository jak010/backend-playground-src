from functools import cached_property

from sqlalchemy import exc
from sqlalchemy.orm import Session

from config.settings import db_session
from src.entity.coupon_entity import CouponEntity
from src.exceptions import ErroCode, CouponIssueException


class CouponRepository:

    def __init__(self, session: Session = db_session):
        self._session: Session = session

    @cached_property
    def session(self):
        return self._session

    def find_by_id_with_lock(self, coupon_id: int) -> CouponEntity:
        query = self.session.query(CouponEntity) \
            .with_for_update() \
            .filter(CouponEntity.id == coupon_id)

        query = query.one_or_none()
        if query is not None:
            return query
        raise Exception()

    def save(self, coupopn_entity: CouponEntity):
        try:
            self.session.add(coupopn_entity)
            self.session.flush()
        except exc.IntegrityError as e:
            raise CouponIssueException(
                ErroCode.DUPLICATE_COUPON_ISSUE,
                message=f"중복"
            )
        return coupopn_entity

    def update(self, coupon: CouponEntity):
        self.session.query(CouponEntity) \
            .filter(CouponEntity.id == coupon.id) \
            .update(coupon.to_dict())
