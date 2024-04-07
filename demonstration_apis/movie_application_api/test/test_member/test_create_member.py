from pytest_bdd import given, when, then, scenario

from src.member import MemberEntity


@scenario("../features/member/member_create.feature", "사용자는 계정을 만들 수 있습니다.")
def test_create_member():
    pass


@given("사용자는 name 을 입력합니다.", target_fixture="member_info")
def initialized_member_info():
    member_info = {
        "name": "test1"
    }
    return member_info


@when("입력된 name과 함께 사용자 entity를 생성합니다.", target_fixture="member_entity")
def create_member_entity(member_info):
    return MemberEntity.new(name=member_info['name'])


@then("생성된 entity는 24자리의 고유 id를 가집니다.")
def verifyed_member_entity_has_a_identity(member_entity):
    assert len(member_entity.member_id) == 24
