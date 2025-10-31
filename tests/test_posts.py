from turtle import title
from app import schemas





def test_get_all_posts(authorized_client, test_posts):
    res=authorized_client.get("/posts/")

    posts_list=list(map(lambda post: schemas.PostWithVotesResponse(**post), res.json()))

    assert res.status_code==200
    assert len(test_posts)==len(posts_list)


def test_unauthorized_user_get_all_posts(client, test_posts):
    res=client.get("/posts/")

    assert res.status_code==401
    

def test_unauthorized_user_get_one_post(client, test_posts):
    res=client.get(f"/posts/{test_posts[0].id}")

    assert res.status_code==401

def test_get_one_post_not_exist(authorized_client, test_posts):
    res=authorized_client.get(f"/posts/{9999}")

    assert res.status_code==404


def test_get_one_post(authorized_client, test_posts):
    print(test_posts)
    res=authorized_client.get(f"/posts/{test_posts[0].id}")
    print(res.json())
    post=schemas.PostWithVotesResponse(**res.json())

    assert post.Post.id==test_posts[0].id
    assert post.Post.content==test_posts[0].content


def test_creat_post(authorized_client, test_user, test_posts):
    res= authorized_client.post("/posts/",
        json={
            "title":"new title",
            "content": "new content"
        }
    )

    created_post=schemas.postResponse(**res.json())

    print(res.json())
    print(created_post)

    assert res.status_code==201
    assert created_post.title=="new title"
    assert created_post.content=="new content"
    assert created_post.published==True #tested the default value
    assert created_post.owner_id==test_user["id"]


def test_unauthorized_user_create_post(client, test_posts, test_user):
    res=client.post("/posts/",
        json={
            "title":"new title",
            "content": "new content"
        }
    )

    assert res.status_code==401

def test_unauthorized_user_delete_post(client, test_posts, test_user):
    res=client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code==401


def test_delete_post(authorized_client, test_posts, test_user):
    res=authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code==204

def test_delete_post_not_exist(authorized_client, test_posts, test_user):
    res=authorized_client.delete(f"/posts/9999")
    assert res.status_code==404

def test_delete_other_user_post(authorized_client, test_posts, test_user):
    res=authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert res.status_code==403

def test_update_post(authorized_client, test_posts, test_user):
    data={
        "title":"updated title",
        "content": "updated_content",
        "id": test_posts[0].id
    }

    res=authorized_client.put(f"/posts/{test_posts[0].id}", json=data)

    updated_post=schemas.postResponse(**res.json())

    assert res.status_code==200
    assert updated_post.title==data["title"]
    assert updated_post.content==data["content"]


def test_update_other_user_post(authorized_client, test_posts, test_user):
    data={
        "title":"updated title",
        "content": "updated_content",
        "id": test_posts[3].id
    }

    res=authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    assert res.status_code==403


def test_unauthorized_user_update_post(client, test_posts, test_user):
    data={
        "title":"updated title",
        "content": "updated_content",
        "id": test_posts[3].id
    }

    res=client.put(f"/posts/{test_posts[3].id}", json=data)    
    assert res.status_code==401

def test_update_post_not_exist(authorized_client, test_posts, test_user):
    data={
        "title":"updated title",
        "content": "updated_content",
        "id": test_posts[0].id
    }

    res=authorized_client.put(f"/posts/9999", json=data)    
    assert res.status_code==404