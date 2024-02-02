from fastapi import FastAPI

from config import orm
from src.controller import root_router
from src.entity import CouponEntity, CouponIssueEntity


def bootstrapping():
    from sqlalchemy.orm import registry
    orm_mapping = registry()
    orm_mapping.map_imperatively(CouponEntity, orm.Coupon)
    orm_mapping.map_imperatively(CouponIssueEntity, orm.CouponIssue)
    return orm_mapping


class CouponIssuranceApplication:
    app = FastAPI(
        title="쿠폰 발급 API"
    )

    def __call__(self, *args, **kwargs):
        bootstrapping()
        self.app.include_router(root_router)

        return self.app


coupon_issurance_application = CouponIssuranceApplication()
